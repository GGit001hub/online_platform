from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Course, Teacher, Lessons, File
from .serializer import CoursSerializer, TeacherSerializer,LessonSerializer
# Create your views here.



class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.filter(status=True)
    serializer_class = CoursSerializer
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data,'------------------')
        # <------ FORIGEN KEY uchun ------>
        product = False
        if 'teacher' in data:
            try:
                product = Teacher.objects.get(full_name=data['teacher'])
            except:
                return Response({'error':"Bunday malumot mavjut emas"})
        # <------ FORIGEN KEY KOD ------>
        try:
            if product:
                new_course = Course.objects.create(
                    name = data['name'],
                    teacher = product,
                    lesson_count = data['lesson_count'],
                    cost = data['cost']
                )
            else:
                new_course = Course.objects.create(
                    name = data['name'],
                    # teacher = product,
                    lesson_count = data['lesson_count'],
                    cost = data['cost']
                )
            new_course.save()
            serializer = CoursSerializer(new_course)
            return Response(serializer.data)
        except:
            return Response({'err':"Malumot to'ldirishda xato ❗"})
        
    def update(self, request, *args, **kwargs):
        data = request.data
        model = self.get_object()
        print(model,'---------',data,'------------')
        try:
            model.name = data['name'] if 'name' in data else model.name
            model.lesson_count = data['lesson_count'] if 'lesson_count' in data else model.lesson_count
            model.cost = data['cost'] if 'cost' in data else model.cost
            model.save()
            serializ = CoursSerializer(model)
            return Response(serializ.data)
        except:
            return Response("❗ Xato ❗")
    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'success':"O'chirish muvofaqiyatli tugadi ✅"})


# Bu yozilgan kodlar TeacherViewset uchun 👇
# Bu yozilgan kodlar TeacherViewset uchun  👇
# Bu yozilgan kodlar TeacherViewset uchun   👇

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(status=True)
    serializer_class = TeacherSerializer
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        data = request.data

        try:
            new_teacher = Teacher.objects.create(
                full_name = data['full_name'],
                age = data['age'],
                degree = data['degree'],
                about = data['about']
            )
            new_teacher.save()
            serializer = TeacherSerializer(new_teacher)
            return Response(serializer.data)
            # return Response({'success':"Yangi teacher yaratildi ✅"})
        except:
            return Response({'error':"Malumot to'ldirishda xatolik"})

    def update(self, request, *args, **kwargs):
        data = request.data
        post = self.get_object()

        try:
            post.full_name = data['full_name'] if 'full_name' in data else post.full_name
            post.age = data['age'] if 'age' in data else post.age
            post.degree = data['degree'] if 'degree' in data else post.degree
            post.about = data['about'] if 'about' in data else post.about
            post.save()
            serializer = TeacherSerializer(post)
            return Response(serializer.data)
        except:
            return Response({'error':"Tahrirlashda xato yuzaga keldi"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'success':"O'chirish yakunlandi"})


# Shu yerdan pasti Lessons uchun yozilgan viewset 👇
# Shu yerdan pasti Lessons uchun yozilgan viewset  👇
# Shu yerdan pasti Lessons uchun yozilgan viewset   👇


class LessonViewset(viewsets.ModelViewSet):
    queryset = Lessons.objects.filter(status=True)
    serializer_class = LessonSerializer
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        data = request.data

        forigen = False
        # file_forign = False
        if 'course' in data:
            try:
                # file_forign = File.objects.get(name=data['files'])
                forigen = Course.objects.get(name=data['course'])
            except:
                return Response({'err':"Xato dars yoki fayl kiritildi"})

        if forigen:
            try:
                new_lesson = Lessons.objects.create(
                    name = data['name'],
                    course = forigen,
                    about = data['about'],
                    video = data['video'],
                    # files = file_forign,
                )
                new_lesson.save()
                serializer = LessonSerializer(new_lesson)
                return Response(serializer.data)
            except:
                return Response({'error':"Malumot to'ldirishda xato yuzaga keldi"})
        return Response({'ok':"Malumotlarni to'ldiring"})
    def update(self, request, *args, **kwargs):
        data = request.data
        model = self.get_object()
        
        curs_forign = False
        file_forign = False
        if 'course' in data :
            try:
                curs_forign = Course.objects.get(name=data['course'])
            except:
                return Response({'err':"Xato kurs kiritildi"})
        if 'files' in data:
            try:
                file_forign = File.objects.get(name=data['files'])
            except:
                return Response({'err':"Xato Fayl kiritildi"})        

        try:
            model.name = data['name'] if 'name' in data else model.name
            model.about = data['about'] if 'about' in data else model.about
            model.video = data['video'] if 'video' in data else model.video
            # model.files = file_forign if 'files' in data else model.files
            model.course = curs_forign if 'course' in data else model.course
            model.save()
            serializer = LessonSerializer(model)
            return Response(serializer.data)
        except:
            return Response({"error":"Malumot to'ldirishda xato"})

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({'success':"O'chirildi "})





