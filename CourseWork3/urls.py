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
    path(r'', views.enter, name = 'enter'),
    path(r'student/<str:student_id>/', views.student, name = 'student'), # student url
    path(r'teacher/<str:teacher_id>/', views.teacher, name = 'teacher'), # teacher url
    path(r'student/<str:student_id>/create_meeting_with_<str:teacher_id>_teacher', views.create_meeting, name = 'create_meeting')
]