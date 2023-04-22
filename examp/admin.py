from django.contrib import admin
from .models import Answer, Question, Quizess, Examp

@admin.register(Examp)
class AxampAmin(admin.ModelAdmin):
    list_display = ['name','lesson','time']


@admin.register(Quizess)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','title']


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['answer_text','is_right']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['quizes','title']
    list_display =['title','quizes','data_update']

    inlines = [AnswerInline,]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text','is_right','question']


