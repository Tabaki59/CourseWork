"""CourseWork3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App_Normocontrol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),  # Main url
    path(r'', views.enter, name = 'enter'),
    path(r'student/<str:student_id>/', views.student, name = 'student'), # student url TODO Сделать фронт и вывод прошлых встреч для чека замечаний + логика записи
    path(r'teacher/<str:teacher_id>/', views.teacher, name = 'teacher'), # teacher url TODO Сделать фронт + систему просмотра встреч и времени и всякое короче
]