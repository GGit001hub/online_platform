from django.contrib import admin
from .models import Course, Teacher, File, Lessons
# Register your models here.



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name','age','degree','status']
    list_editable = ['status']



class FleAdmin(admin.StackedInline):
    model = File



@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name','course','status']
    list_editable = ['status']
    inlines = [FleAdmin]
    
    class Meta:
        model = Lessons


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','id','teacher','lesson_count','slug']
