from django.contrib import admin
from .models import Student,MyCourse
# Register your models here.

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['username','age','email','gender','status']
    list_editable = ['status']


@admin.register(MyCourse)
class Ciasdsad(admin.ModelAdmin):
    list_display = ['student','course','ball','coin']
