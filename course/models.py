from django.db import models
from autoslug import AutoSlugField
# Create your models here.



class Teacher(models.Model):
    full_name = models.CharField(max_length=111)
    age = models.PositiveIntegerField()
    slug = AutoSlugField(populate_from = 'full_name',unique=True)
    degree = models.CharField(max_length=51)# teacher darajasi
    about = models.TextField()
    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name



class Course(models.Model):
    name = models.CharField(max_length=111,unique=True)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    lesson_count = models.PositiveIntegerField()
    cost = models.PositiveIntegerField(verbose_name='pul uchun',null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class Lessons(models.Model):
    name = models.CharField(max_length=61)
    slug = AutoSlugField(populate_from = 'name',unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course')
    about = models.TextField()
    video = models.FileField(upload_to='vid_cours/')
    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class File(models.Model):
    name = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='fils')
    fille = models.FileField(upload_to='img_cours/')

    # def __str__(self) -> str:
    #     return self.name