from django.db import models
from course.models import Lessons
from autoslug import AutoSlugField
from student.models import Student
# Create your models here.


class Examp(models.Model):
    name = models.CharField(max_length=111)
    slug = AutoSlugField(populate_from = 'name',unique=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE,related_name='lsn')
    about = models.TextField()
    time = models.PositiveIntegerField(verbose_name='Vaqt',null=True)

    def __str__(self) -> str:
        return self.name


class Quizess(models.Model):
    examp = models.ForeignKey(Examp, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default='New Quizs')
    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['id']

class Update(models.Model):
    data_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(Update):
    class Meta:
        ordering = ['id']

    SCALE = (
        (0, ('Fundamental')),
        (1, ('Beginer')),
        (2, ('Intermediate')),
        (3, ('Advanced')),
        (4, ('Expert')),
    )
    TYPE = (
        (0,('Multiple choice')),
    )

    technique = models.IntegerField(choices=TYPE,default=0)
    quizes = models.ForeignKey(Quizess, related_name='question',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=123)
    difficulty = models.IntegerField(choices=SCALE,default=0,verbose_name="Difficulty")
    deta_craeted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name='Active status')

    def __str__(self) -> str:
        return self.title


class Answer(Update):
    class Meta:
        verbose_name = 'Ansver'
        ordering = ['id']
    question = models.ForeignKey(Question,related_name='answer',on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=221,verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer_text




