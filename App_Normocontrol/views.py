from django.shortcuts import render
from django.urls import reverse, resolve
from .models import Students, Teachers, Meeting, Work
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def enter(request, href):
    if request.method == 'POST':
        user_login = request.POST['user_login']
        password = request.POST['password']

        t = Teachers.objects.get(login=user_login, password=password)
        if t is not None:
            id = t.teacher_id
            href = '/teacher/' + str(t.teacher_id)
            return HttpResponseRedirect(reverse(href))
            # return request, href
            # return HttpResponse(href)
            # return teacher(request, id)
            # return HttpResponseRedirect(reverse(teacher , args= id ))
            # return HttpResponseRedirect(resolve(href))
            # return render(request, 'teachers.html', {'href': href})

        s = Students.objects.get(login=user_login, student_id=password)
        if s is not None:
            id = s.student_id
            href = 'student/' + str(s.student_id)
            return HttpResponseRedirect(reverse(href))
            # return HttpResponse(href)
            # return request, href
            # return student(request, id)
            # return HttpResponseRedirect(reverse(student, args= id))
            # return HttpResponseRedirect(resolve(href))
            # return render(request, 'student.html', {'href': href})

        else:
            href = ""
            return HttpResponseRedirect(reverse(href))


# Function for student form  TODO Вытащить на вьюшку переключение по дням недели с датами, там сслка будет менять день в зависимости от него вытаскивать нужный интервал
def student(request, student_id):
    teachers = Teachers.objects.order_by()
    return render(request, 'student.html', {'teachers': teachers})

def create_meeting(request, teacher_id):
    pass

# Function for teacher's view TODO make meetings and shift for meeting html
def teacher(request, teacher_id):
    students_list = Students.objects.order_by()
    return  render(request, 'teacher.html', {'students_list': students_list})