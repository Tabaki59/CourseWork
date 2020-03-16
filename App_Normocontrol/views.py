from django.shortcuts import render
from django.urls import reverse, resolve
from .models import Students, Teachers, Meeting, Work
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def enter(request):
    flag_1 = False
    flag_2 = False
    if request.method == 'POST':
        user_login = request.POST.get('user_login', '')
        password = request.POST.get('password', '')

        try:
            t = Teachers.objects.get(login=user_login, password=password)
            flag_1 = True
        except ObjectDoesNotExist:
            flag_1 = False
        try:
            s = Students.objects.get(login=user_login, student_id=password)
            flag_2 = True
        except ObjectDoesNotExist:
            flag_2 = False

        if (flag_1):
            t = Teachers.objects.get(login=user_login, password=password)
            return HttpResponseRedirect(reverse(teacher, args=(str(t.teacher_id))))

        if (flag_2):
            s = Students.objects.get(login=user_login, student_id=password)
            return HttpResponseRedirect(reverse(student, kwargs={"student_id": s.student_id}))
        if not flag_1 and not flag_2:
            return render(request, 'base.html')

    else:
        return render(request, 'base.html')


# Function for student form  TODO Вытащить на вьюшку переключение по дням недели с датами, там сслка будет менять
#  день в зависимости от него вытаскивать нужный интервал
def student(request, student_id):
    teachers = Teachers.objects.order_by()
    return render(request, 'student.html', {'teachers': teachers})


def create_meeting(request, teacher_id):
    pass


# Function for teacher's view TODO make meetings and shift for meeting html
def teacher(request, teacher_id):
    students_list = Students.objects.order_by()
    return render(request, 'teacher.html', {'students_list': students_list})
