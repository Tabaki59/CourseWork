from django.shortcuts import render
from .models import Students, Teachers, Meeting, Work, Freetime

# Create your views here.
def index(request):
    return render(request, 'base.html')

# Function for authorization TODO make return path for student or teacher
def login(request, login, password):
    pass

# Function for student form
def student(request):
    teachers_time_list = Teachers.objects.order_by()
    return render(request, 'student.html', {'teachers_time_list': teachers_time_list})

# Function for teacher's view TODO make meetings and shift for meeting html
def teacher(request):
    students_list = Students.objects.order_by()
    return  render(request, 'teacher.html', {'students_list': students_list})