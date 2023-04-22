from rest_framework import serializers
from .models import Course, Teacher, File, Lessons


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','teacher','lesson_count','cost','slug']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name','age','degree','about','slug']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['fille',]



class LessonSerializer(serializers.ModelSerializer):
    imagine = FileSerializer(many=True, read_only=True)
    class Meta:
        model = Lessons
        fields = ['id','name','course','video','about',"imagine",'slug']


