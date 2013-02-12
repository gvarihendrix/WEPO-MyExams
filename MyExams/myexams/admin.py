from django.contrib import admin
from myexams.models import *
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Semester)
admin.site.register(StudentCourses)
admin.site.register(Exam)
admin.site.register(Answer)
admin.site.register(ExamsTaken)
admin.site.register(Selection)
