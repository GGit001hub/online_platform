from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Answer, Question, Quizess, Examp
from .serializer import QuizSerializer, RandomQuestionSerializer
from .serializer import QuizQuestionSerializer

class Quizs(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizess.objects.all()


class RandomQuizs(APIView):

    def get(self, request, fomat=None, **kwargs):
        question = Question.objects.filter(quizes__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)

class QuestionQuiz(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quizes__title=kwargs['topic'])
        serializer = QuizQuestionSerializer(quiz, many=True)
        return Response(serializer.data)