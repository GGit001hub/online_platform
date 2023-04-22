from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from course.models import Course
from .models import Student, MyCourse
from .serializer import (RegiseterSerializer, LoginSerializer,
                         ProfileSerializer,ProfileUpdateSerializer,
                         PasswordChangeSerializer,SendResetPasswordSerializer,
                         ResetPasswordSerializer,MycourseSerializer)
from .rendere import UserRenderer
# Create your views here.


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }


class RegisterView(views.APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = RegiseterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({'token':token,'success':"Siz muvofaqiyatli ro'yxatdan o'tdingiz"})
        return Response({'error':"Ro'yxatdan o'tish uchun malumotlarni to'ldiring"})


class LoginView(views.APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializr = LoginSerializer(data=request.data)
        if serializr.is_valid(raise_exception=True):
            username = serializr.data.get('username')
            password = serializr.data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                token = get_token_for_user(user)
                return Response({'token':token,'success':"Login amalga oshdi"})
            else:
                return Response({'error':"Username yoki parol xato "})
        else:
            return Response(serializr.errors)

class ProfileView(views.APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = ProfileSerializer(request.user)
        print(serializer,'----------------++++++++++++++')
        return Response(serializer.data)

class ProfileUpdateView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        data = request.data
        model = self.get_object()
        if 'username' in data:
            category = Student.objects.filter(status=True)
            for ctg in category:
                if ctg.username == data['username']:
                    return Response({'error':"Bunday username oldindan mavjut"})

        model.username = data['username'] if 'username' in data else model.username
        # model.password = data['password'] if 'password' in data else model.password
        model.phone = data['phone'] if 'phone' in data else model.phone
        model.email = data['email'] if 'email' in data else model.email
        model.age = data['age'] if 'age' in data else model.age

        model.save()
        serializer = ProfileUpdateSerializer(model)
        return Response(serializer.data)

class PaswordChangeView(views.APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid():
            return Response({'success':"Parol Almashtirildi "})
        return Response(serializer.errors)

class SendResetPasswordView(views.APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        seializer = SendResetPasswordSerializer(data=request.data)
        if seializer.is_valid(raise_exception=True):
            return Response({'send':"Kiritilgan emailga kod yuborildi"})
        return Response(seializer.errors)

class ResetPasswordView(views.APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = ResetPasswordSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'success':"Password Change Successfull"})
        return Response(serializer.errors)

class MyCoureseView(viewsets.ModelViewSet):
    queryset = MyCourse.objects.all()
    serializer_class = MycourseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        father_st = False
        father_crs = False

        if 'student' in data:
            father_st = Student.objects.get(username=data['student'])
        else:
            return Response({'st':"Bunday student topilmadi"})
        
        if 'course' in data:
            father_crs = Course.objects.get(name=data['course'])
        else:
            return Response({'crs':"Bunday Cours haqida malumot yo'q"})
        

        if father_crs and father_st:
            try:
                new_course = MyCourse.objects.create(
                    student=father_st,
                    course=father_crs,
                    ball=data['ball'],
                    coin=data['coin'],
                )
                new_course.save()
                serializer = MycourseSerializer(new_course)
                return Response(serializer.data)
                # return Response({'success':"Yangi course yaratildi"})
            except:
                return Response({'error':"Malumot to'ldirishda xato yuzaga keldi"})

    def update(self, request, *args, **kwargs):
        data = request.data
        model = self.get_object()

        father_std = False
        father_crs = False

        if 'student' in data:
            try:
                father_std = Student.objects.get(username=data['student'])
            except:
                return Response({'std':"Noto'g'ri student kiritildi"})
        if 'course' in data:
            try:
                father_crs = Course.objects.get(name=data['course'])
            except:
                return Response({'crs':"Noto'g'ri Course kiritildi"})
        try:
            model.student = father_std if 'student' in data else model.student
            model.course = father_crs if 'course' in data else model.course
            model.ball = data['ball'] if 'ball' in data else model.ball
            model.coin = data['coin'] if 'coin' in data else model.coin
            model.save()
            serizlizer = MycourseSerializer(model)
            return Response(serizlizer.data)
        except:
            return Response({'error':"Noto'gri malumot kiritildi"})

    def destroy(self, request, *args, **kwargs):
        udalet = self.get_object()
        udalet.delete()
        return Response({'delete':"O'chirildi ✅"})
