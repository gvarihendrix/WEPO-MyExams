from django.db import models
from django.contrib.auth.models import User
from pprint import pprint
import datetime


class Student(models.Model):
    person   = models.ForeignKey(User)
    enrolled = models.DateTimeField('Date enrolled')

    def __unicode__(self):
        return u'%s %s %s Date enrolled: %s' %(self.person.first_name, self.person.last_name, self.person.username, self.enrolled)

class Teacher(models.Model):
    person   = models.ForeignKey(User)
    hired    = models.DateTimeField('Date hired')

    def __unicode__(self):
        return u'%s %s %s Date hired: %s' %(self.person.first_name, self.person.last_name, self.person.username ,self.hired)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name


class Semester(models.Model):
    year   = models.DateField()
    season = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s %s' % (self.year, self.season)


class Course(models.Model):
    teacher  = models.ForeignKey(Teacher)
    semester = models.ForeignKey(Semester)
    school   = models.ForeignKey(School)
    name     = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.teacher, self.semester)


# Student can take many courses and there can be many courses available
class StudentCourses(models.Model):
    course  = models.ForeignKey(Course)
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return u'%s is enrolled in %s semester %s' % (self.student.person.first_name, self.course.name, self.course.semester.year)


# Exams
class Exam(models.Model):
    course       = models.ForeignKey(Course)
    exam_name    = models.CharField(max_length=100)
    date_created = models.DateField()
    return_date  = models.DateField()
    
    # __unicode__ method like shown in Django tutorial
    def __unicode__(self):
        return u'%s %s %s' % (self.exam_name, self.date_created, self.return_date)


# Question to an exam
class Question(models.Model):
    exam     = models.ForeignKey(Exam)
    question = models.CharField(max_length=1000)
    number   = models.IntegerField(null=True) # For ordering
    value    = models.IntegerField(null=True)
    
    # __unicode__ method like shown in Django tutorial
    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question   = models.ForeignKey(Question)
    answer     = models.CharField(max_length=1000)
    number     = models.IntegerField(null=True)
    is_correct = models.BooleanField()

    # __unicode__ method like shown in Django tutorial
    def __unicode__(self):
        return self.answer   



class ExamsTaken(models.Model):
    exam          = models.ForeignKey(Exam)
    student       = models.ForeignKey(Student)
    date_finished = models.DateField()
    exams_grade   = models.FloatField()

    class Meta:
        ordering = ['-exam', 'student']

    def get_rank(self):
        exams_taken = ExamsTaken.objects.filter(exam=self.exam)
        higher = 0
        same   = 0

        for exam in exams_taken:
            if(self.exams_grade == exam.exams_grade):
                same += 1
            elif(self.exams_grade < exam.exams_grade):
                higher +=1

        total = len(exams_taken)
        rank = str(higher + 1)

        if(same > 1):
            rank += '-' + str(higher + same)
        pprint(total)
        return rank + '/' + str(total)


class Selection(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    name  = models.CharField(max_length=20)

    def __unicode__(self):
        return self.answer