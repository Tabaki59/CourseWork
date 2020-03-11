# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Group(models.Model):
    group_id = models.IntegerField(db_column='Group_id', primary_key=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=5)  # Field name made lowercase.

    def __str__(self):
        return self.group

    class Meta:
        managed = False
        db_table = 'Group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Meeting(models.Model):
    meeting_id = models.IntegerField(db_column='Meeting_id', primary_key=True)  # Field name made lowercase.
    meeting_time = models.TimeField(db_column='Meeting_time')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='Student')  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher')  # Field name made lowercase.
    meeting_status = models.ForeignKey('MeetingStatus', models.DO_NOTHING, db_column='Meeting_status')  # Field name made lowercase.
    #
    # def __str__(self):
    #     return self.student + self.teacher + self.meeting_time
    #
    class Meta:
        managed = False
        db_table = 'Meeting'


class MeetingStatus(models.Model):
    status_id = models.IntegerField(db_column='Status_id', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.

    def __str__(self):
        return self.status

    class Meta:
        managed = False
        db_table = 'Meeting_status'


class School(models.Model):
    school_id = models.IntegerField(db_column='School_id', primary_key=True)  # Field name made lowercase.
    school = models.TextField(db_column='School')  # Field name made lowercase.

    def __str__(self):
        return self.school

    class Meta:
        managed = False
        db_table = 'School'
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Students(models.Model):
    student_id = models.CharField(db_column='Student_id', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='Group')  # Field name made lowercase.
    work = models.ForeignKey('Work', models.DO_NOTHING, db_column='Work')  # Field name made lowercase.
    course = models.IntegerField(db_column='Course')  # Field name made lowercase.
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='School')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    login = models.TextField(db_column='Login')  # Field name made lowercase.

    def __str__(self):
        return str(self.name) + str(self.group)

    class Meta:
        managed = False
        db_table = 'Students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teachers(models.Model):
    teacher_id = models.IntegerField(db_column='Teacher_id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone')  # Field name made lowercase.
    freetime_b = models.TimeField(db_column='FreeTime_b')  # Field name made lowercase.
    freetime_e = models.TimeField(db_column='FreeTime_e')  # Field name made lowercase.
    login = models.TextField(db_column='Login')  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Teachers'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Work(models.Model):
    type_id = models.IntegerField(db_column='Type_id', primary_key=True)  # Field name made lowercase.
    type_name = models.TextField(db_column='Type_name')  # Field name made lowercase.
    general_criteria = models.TextField(db_column='General_criteria')  # Field name made lowercase.
    titles_criteria = models.TextField(db_column='Titles_criteria')  # Field name made lowercase.
    lists_criteria = models.TextField(db_column='Lists_criteria')  # Field name made lowercase.
    tables_criteria = models.TextField(db_column='Tables_criteria')  # Field name made lowercase.
    formulas_criteria = models.TextField(db_column='Formulas_criteria')  # Field name made lowercase.
    pictures_criteria = models.TextField(db_column='Pictures_criteria')  # Field name made lowercase.
    literature_criteria = models.TextField(db_column='Literature_criteria')  # Field name made lowercase.
    applications_criteria = models.TextField(db_column='Applications_criteria')  # Field name made lowercase.

    def __str__(self):
        return self.type_name

    class Meta:
        managed = False
        db_table = 'Work'
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работы'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
