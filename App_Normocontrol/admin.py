from django.contrib import admin

# Register your models here.
from .models import Work, School, Students, Group, Teachers, Freetime
admin.site.register(Work)
admin.site.register(School)
admin.site.register(Students)
admin.site.register(Group)
admin.site.register(Teachers)
admin.site.register(Freetime)