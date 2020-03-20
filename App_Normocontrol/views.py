from django.shortcuts import render
from django.urls import reverse
from django.utils.dateparse import parse_date, parse_time
from .models import Students, Teachers, Meeting, Work, MeetingStatus
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from datetime import datetime, date, timedelta


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


# Создание встречи (Готова)
def create_meeting(request, student_id, teacher_id):  # Все проверки готовы
    s = Students.objects.get(student_id=student_id)
    t = Teachers.objects.get(teacher_id=teacher_id)
    m = Meeting.objects.filter(teacher=t.teacher_id, meeting_status=1)
    status = MeetingStatus.objects.get(status_id=1)
    error = False
    duration = timedelta(minutes = 15)
    if request.method == 'POST':
        time = parse_time(request.POST.get('time', ''))
        if t.free_beg > time or time > t.free_end:
            error = True
            return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error, 'meeting': m})
        else:
            if not Meeting.objects.all():
                meet_id = 1
            else:
                if not Meeting.objects.filter(student=s.student_id, meeting_status=status.status_id):
                    teachers_meeting_today = Meeting.objects.filter(teacher=t.teacher_id)
                    for obj in teachers_meeting_today:
                        if obj.meeting_time < time < (obj.meeting_time + duration).time():
                            error = True
                            return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error, 'meeting': m})
                    max_id = Meeting.objects.order_by('meeting_id').last()
                    meet_id = max_id.meeting_id + 1
                    m = Meeting.objects.create(meeting_id=meet_id, meeting_time=time, student=s, teacher=t,
                                               meeting_status=status)  # В случае с учитeлем и студентом передаем экземипляр
                    return HttpResponseRedirect(reverse(student, kwargs={"student_id": s.student_id}))
                else:
                    error = True
                    return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error, 'meeting': m})
    else:
        return render(request, 'create_meeting.html', {'teacher': t, 'student': s, 'error': error, 'meeting': m})


# Вьюха препода (В целом готова)
def teacher(request, teacher_id):
    t = Teachers.objects.get(teacher_id = teacher_id)
    m = Meeting.objects.filter(teacher=t.teacher_id, meeting_status=1)
    if request.method == 'POST':
        begin = parse_time(request.POST.get('begin', ''))
        end = parse_time(request.POST.get('end', ''))
        dif_beg = datetime.combine(date.min, begin) - datetime.combine(date.min, t.free_beg)
        t.free_beg = begin
        t.free_end = end
        t.save()
        for obj in m:
            new_time = (datetime.combine(date.min, obj.meeting_time) + dif_beg).time()
            if begin > new_time or new_time > end:
                del_obj = Meeting.objects.get(meeting_id = obj.meeting_id)
                del_obj.delete()
                # obj.delete()
            else:
                obj.meeting_time = new_time
                obj.save()
    return render(request, 'teacher.html', {'teacher': t,'meeting': m})


# Непосредственно проверка работы (Готова)
def check(request, teacher_id, meeting_id):
    t = Teachers.objects.get(teacher_id = teacher_id)
    m = Meeting.objects.get(meeting_id = meeting_id)
    s = Students.objects.get(**{"student_id": m.student_id})
    w = Work.objects.get(type_name = s.work)
    status = MeetingStatus.objects.get(status_id=2)
    if request.method == 'POST':
        notes = 'Есть замечания в: '
        errors = request.POST.getlist('errors')
        for e in errors:
            notes += e
        notes += request.POST.get('notes')
        m.notes = notes
        m.meeting_status = status
        m.save()
        return HttpResponseRedirect(reverse(teacher, args=(str(t.teacher_id))))
    return render(request, 'check_meeting.html', {'teacher': t, 'meeting': m, 'student': s, 'work': w})