from django.shortcuts import render
from django.urls import reverse, resolve
from django.utils.dateparse import parse_date, parse_time
from .models import Students, Teachers, Meeting, Work, MeetingStatus
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
import datetime


# Функция входа в систему (Готова)
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
            login_incorrect = True
            return render(request, 'base.html', {'login_incorrect': login_incorrect})

    else:
        return render(request, 'base.html')


# Вьюха студента (Готова)
def student(request, student_id):
    s = Students.objects.get(student_id=student_id)
    t = Teachers.objects.all()
    m = Meeting.objects.filter(student=s.student_id)
    return render(request, 'student.html', {'teachers': t, 'student': s, 'meetings': m})


# Создание встречи (Готова но тесты пока не все проведены) TODO Протестировать проверки хотя итак работает все
def create_meeting(request, student_id, teacher_id):  # Все проверки готовы
    s = Students.objects.get(student_id=student_id)
    t = Teachers.objects.get(teacher_id=teacher_id)
    status = MeetingStatus.objects.get(status_id=1)
    error = False
    duration = datetime.time(minute=15)
    if request.method == 'POST':
        time = parse_time(request.POST.get('time', ''))
        if t.free_beg > time > t.free_end:
            error = True
            return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error})
        else:
            if not Meeting.objects.all():
                meet_id = 1
            else:
                if not Meeting.objects.filter(student=s.student_id, meeting_status=status.status_id):
                    teachers_meeting_today = Meeting.objects.filter(teacher=t.teacher_id)
                    for obj in teachers_meeting_today:
                        if obj.meeting_time < time < (obj.meeting_time + duration):
                            error = True
                            return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error})
                    meet_id = Meeting.objects.aggregate(Max('meeting_id')) + 1
                    m = Meeting.objects.create(meeting_id=meet_id, meeting_time=time, student=s, teacher=t,
                                               meeting_status=status)  # В случае с учитилем и студентом не передаем поле, передаем экземипляр
                    return HttpResponseRedirect(reverse(student, kwargs={"student_id": s.student_id}))
                else:
                    error = True
                    return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error})
    else:
        return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error})


# Вьюха препода TODO Сделать список встреч со ссылкой на начало ее и редачить время
def teacher(request, teacher_id):
    return render(request, 'teacher.html', {})

# TODO Вьюха для самого процесса контроля
def check():
    pass