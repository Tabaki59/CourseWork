from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Group(models.Model):
    group_id = models.IntegerField(db_column='Group_id', primary_key=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group'


class Meeting(models.Model):
    meeting_id = models.IntegerField(db_column='Meeting_id', primary_key=True)  # Field name made lowercase.
    meeting_time = models.TimeField(db_column='Meeting_time')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='Student')  # Field name made lowercase.
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='Teacher')  # Field name made lowercase.
    meeting_status = models.ForeignKey('MeetingStatus', models.DO_NOTHING, db_column='Meeting_status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Meeting'


class MeetingStatus(models.Model):
    status_id = models.IntegerField(db_column='Status_id', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Meeting_status'


class School(models.Model):
    school_id = models.IntegerField(db_column='School_id', primary_key=True)  # Field name made lowercase.
    school = models.TextField(db_column='School')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'School'


class Students(models.Model):
    student_id = models.CharField(db_column='Student_id', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='Group')  # Field name made lowercase.
    work = models.ForeignKey('Work', models.DO_NOTHING, db_column='Work')  # Field name made lowercase.
    course = models.IntegerField(db_column='Course')  # Field name made lowercase.
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='School')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    login = models.TextField(db_column='Login')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'


class Teachers(models.Model):
    teacher_id = models.IntegerField(db_column='Teacher_id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone')  # Field name made lowercase.
    meeting_time_begin = models.TimeField(db_column='Meeting_time_begin')  # Field name made lowercase.
    meeting_time_end = models.TimeField(db_column='Meeting_time_end')  # Field name made lowercase.
    login = models.TextField(db_column='Login')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teachers'


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

    class Meta:
        managed = False
        db_table = 'Work'
