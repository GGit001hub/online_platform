from rest_framework import serializers
from .models import Quizess, Question, Answer, Examp

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizess
        fields = ['title']



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','answer_text','is_right']


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['title','answer']


class QuizQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['title','answer']

