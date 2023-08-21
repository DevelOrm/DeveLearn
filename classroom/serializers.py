from rest_framework import serializers
from .models import Classroom, Test, LectureNote, Question, Comment, TestSubmit


class ClassroomSerializer(serializers.ModelSerializer):
    # tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Classroom
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class LectureNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNote
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TestSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSubmit
        fields = '__all__'
