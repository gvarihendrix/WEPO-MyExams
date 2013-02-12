
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import *
from myexams.models import *
from myexams.helper import is_teacher
from django.contrib.auth.decorators import login_required

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
    user = request.user
    return render_to_response('myexams/teacher.html', {'courses': courses, 'user':user})

@login_required
def student(request):
    student_courses = StudentCourses.objects.filter(student__person__username=request.user.username)
    user = request.user
    
    return render_to_response('myexams/student.html', {'student_courses': student_courses, 'user':user})


@login_required
def course(request, course_id):
    exams = Exam.objects.filter(course__id=course_id)
    c =     Course.objects.get(pk=course_id)
    return render_to_response('myexams/course.html', {'course': c,'exams': exams ,'user': request.user})

@login_required
def exam(request, exam_id):
    questions = Question.filter(exam__id=exam_id)

    return render_to_response('myexams/exam.html', {'questions': questions, 'user': request.user})

@login_required
def results(request, exam_id):
    pass


@login_required
def score(request, exam_id):
    pass