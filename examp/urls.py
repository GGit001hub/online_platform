from django.urls import path, include
from .views import Quizs,RandomQuizs,QuestionQuiz

urlpatterns = [
    path('',Quizs.as_view()),
    path('r/<str:topic>/',RandomQuizs.as_view()),
    path('q/<str:topic>/',QuestionQuiz.as_view())
]
