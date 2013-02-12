from models import Teacher

# is the user a teacher if so return true
def is_teacher(user):
    teachers = Teacher.objects.all()

    for teacher in teachers:
        if(teacher.person.username == user.username):
            return True   
    
    return False 