from django.shortcuts import render
from .models import Students, Teachers, Meeting, Work
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'base.html', {'form': form})

# Function for student form  TODO Вытащить на вьюшку переключение по дням недели с датами, там сслка будет менять день в зависимости от него вытаскивать нужный интервал
def student(request):
    teachers = Teachers.objects.order_by()
    return render(request, 'student.html', {'teachers': teachers})

def create_meeting(request, teacher_id):
    pass

# Function for teacher's view TODO make meetings and shift for meeting html
def teacher(request):
    students_list = Students.objects.order_by()
    return  render(request, 'teacher.html', {'students_list': students_list})