from django.shortcuts import *
from myexams.models import *
from myexams.helper import is_teacher
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime

# Create your views here.


@login_required
def index(request):
    # On index cheack if user is teacher or student
    if is_teacher(request.user):
        return teacher(request)
    else:
        return student(request)


@login_required
def teacher(request):
    courses = Course.objects.filter(teacher__person__username=request.user.username)
    return render_to_response('myexams/teacher.html',
        {'courses': courses, 'user': request.user})


@login_required
def student(request):
    if is_teacher(request.user):
        return teacher(request)

    student_courses = StudentCourses.objects.filter(student__person__username=request.user.username)
    return render_to_response('myexams/student.html',
        {'student_courses': student_courses, 'user': request.user})


@login_required
def course(request, course_id):
    if is_teacher(request.user):
        return teacher(request)

    exams = Exam.objects.filter(course__id=course_id)

    exams_taken = ExamsTaken.objects.filter(student__username=request.user.username)

    avg_grade = 0
    for exam_t in exams_taken:
        exams = exams.exclude(id=exam_t.exam.id)
        avg_grade += exam_t.exams_grade

    exams = exams.exclude(return_date__lte=datetime.datetime.now())
    len_exams_taken = len(exams_taken) if len(exams_taken) > 0 else 1

    avg_grade /= len_exams_taken
    c = Course.objects.get(pk=course_id)

    return render_to_response('myexams/course.html',
        {'course': c, 'exams': exams, 'user': request.user,
        'exams_taken': exams_taken, 'avg_grade': avg_grade})


@login_required
def exams(request, exam_id):

    if is_teacher(request.user):
        return teacher(request)

    exam = Exam.objects.get(pk=exam_id)
    return render_to_response('myexams/exam.html',
        {'exam': exam, 'user': request.user},
        context_instance=RequestContext(request))


@login_required
def new(request, course_id):

        if not is_teacher(request.user):
                return index(request)

        exam = Exam()
        exam.course__id = course_id
        exam.name = ""
        exam.date_created = datetime.datetime.now()
        exam.return_date = datetime.datetime.now() + datetime.timedelta(days=7)
        return render_to_response('myexams/new_exam.html',
            {'exam': exam}, context_instance=RequestContext(request))


@login_required
def create(request):

    if not is_teacher(request.user):
            return index(request)

    exam = Exam()
    exam.course_id = request.POST['id']
    exam.exam_name = request.POST['exam_name']
    exam.date_created = datetime.datetime.now()
    exam.return_date = request.POST['exam_return_date']
    exam.save()

    q_count = 1
    #find posted questions
    while(True):
        que_post = 'question_' + str(q_count)
        if que_post in request.POST:
            web_question = request.POST[que_post]
            question_value = request.POST['val_' + que_post]
            question = exam.question_set.create(question=web_question, number=q_count, value=question_value)
            a_count = 1
            #find posted answers
            while(True):
                ans_post = 'answer_' + str(q_count) + '_' + str(a_count)
                if ans_post in request.POST:
                    print ans_post
                    web_answer = request.POST[ans_post]

                    #check if answer is correct
                    correct = False
                    chk_post = 'answer_ck_' + str(q_count) + '_' + str(a_count)
                    if chk_post in request.POST:
                        correct = True

                    question.answer_set.create(answer=web_answer, number=0, is_correct=correct)
                else:
                    break
                a_count += 1
        else:
            break
        q_count += 1

    exam.save()

    return HttpResponseRedirect(reverse('myexams.views.index'))


@login_required
def submit(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)

    for question in exam.question_set.all():
        try:
            request.POST['question_' + str(question.id)]
        except:
            return render_to_response('exams/show.html',
                {'exam': exam,
                'error_message': "You didn't select all choices.",
                }, context_instance=RequestContext(request))

    total_questions = exam.question_set.count()
    # save guard for divbyzero,
    # but exam should not have have zero questions
    if total_questions == 0:
        return render_to_response('myexams/exam.html', {'exam': exam,
            'error_message': "Exam has no questions.",
            }, context_instance=RequestContext(request))

    for exam_taken in ExamsTaken.objects.filter(exam__id=exam_id):
        if exam_taken.has_taken_exam and exam_taken.student == request.user:
            return render_to_response('myexams/exam.html', {'exam': exam,
            'error_message': "You have already taken this exam.",
                }, context_instance=RequestContext(request))

    total_correct_value = 0
    total_value = 0

    for question in exam.question_set.all():
            total_value += question.value
            answer = question.answer_set.get(pk=request.POST['question_' +
                str(question.id)])
            if answer.is_correct:
                    total_correct_value += question.value
    if(total_value == 0):
            total_value = 1
            #no div by zero pleas
    grade = float((float(total_correct_value) / float(total_value)) * 10)

    te = ExamsTaken(exam=exam, student=request.user, date_finished=datetime.datetime.now(), exams_grade=float(grade), has_taken_exam=True)
    te.save()
    return HttpResponseRedirect(reverse('exam_result', args=(te.id,)))
