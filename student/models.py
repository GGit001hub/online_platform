from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from course.models import Course


# Create your models here.


GENDER = (
    ('woman',"Ayol"),
    ('man',"Erkak")
)


class Student(AbstractUser):
    username = models.CharField(max_length=51,unique=True)
    slug = AutoSlugField(populate_from='username',unique=True)
    age = models.PositiveIntegerField(verbose_name="Yoshingiz")
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12,verbose_name='phone number')
    gender = models.CharField(max_length=111,choices=GENDER)
    ball = models.PositiveBigIntegerField(default=0)
    coin = models.PositiveIntegerField(default=0)
    password2 = models.CharField(max_length=123,default='0')
    
    last_name = False
    first_name =False
    REQUIRED_FIELDS = ['email','phone','age','gender']
    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username




class MyCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='my_cours')
    ball = models.PositiveIntegerField(default=0)
    coin = models.PositiveIntegerField(default=0)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

 