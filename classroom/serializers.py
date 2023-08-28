from rest_framework import serializers
from .models import Classroom, Test, TestBoard, TestComment, LectureNote, LectureNoteBoard, LectureNoteComment, \
    Question, QuestionBoard, QuestionComment, TestSubmit

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view, extend_schema_field, OpenApiTypes

class ClassroomSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')  # 초단위를 포함하지 않도록 형식 지정
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')  # 초단위를 포함하지 않도록 형식 지정

    class Meta:
        model = Classroom
        fields = '__all__'


class TestBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBoard
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestComment
        fields = '__all__'


class LectureNoteBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNoteBoard
        fields = '__all__'


class LectureNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNote
        fields = '__all__'


class LectureNoteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureNoteComment
        fields = '__all__'


class QuestionBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBoard
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
