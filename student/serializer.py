from rest_framework import serializers
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from xml.dom import ValidationErr
from .models import Student, MyCourse
from .utils import Util




class RegiseterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Student
        fields = ['username','email','phone','gender', 'age', 'password','password2','ball','coin']
        extra_kvarws = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Parol bir xil bo'lishi kerak")
        return attrs
    
    def create(self, validated_data):
        print(validated_data,'--------------')
        return Student.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = Student
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username','email','age','gender','phone','password']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username','email','age','phone','slug']

class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Student
        fields = ['password','password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Parol xato kiritildi ")
        user.set_password(password)
        user.save()
        return attrs


class SendResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Student
        fields = ['email',]
    def validate(self, attrs):
        email = attrs.get('email')
        if Student.objects.filter(email=email).exists():
            user = Student.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://localhost:8000/student/reset-password/"+uid+'/'+token
            body = "Quyidagi manzilga kirib parolni almashtiring" + link
            
            data = {
                'subject':'Rest password',
                'body':body,
                'to_email':user.email,
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationErr("Emailga yuborib bo'lmadi")
            

class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Student
        fields = ['password','password2']
    
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
                
            if password != password2:
                raise serializers.ValidationError("Parol xato kiritildi !!!")
            id = smart_str(urlsafe_base64_decode(uid))
            user = Student.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr('Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
            PasswordResetTokenGenerator().check_token(user, token) 
            raise ValidationErr('Token is not Valid or Expired')


class MycourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = ['id','student','course','ball','coin']
