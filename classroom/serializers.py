from rest_framework import serializers
from .models import Classroom, Test, Board, TestComment, LectureNote, LectureNoteComment, Question, QuestionComment, \
    TestSubmit, Subscription


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestComment
        fields = '__all__'


class LectureNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNote
        fields = '__all__'


class LectureNoteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNoteComment
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = '__all__'


class TestSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSubmit
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
