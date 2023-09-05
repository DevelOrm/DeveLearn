from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Classroom, Test, Board, TestComment, LectureNote, LectureNoteComment, Question, QuestionComment, \
    TestSubmit, Subscription

User = get_user_model


class ClassroomSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='classroom.user.nickname', read_only=True)
    classroom_name = serializers.CharField(source='classroom.class_name', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Board
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='board.classroom.class_name', read_only=True)
    board_name = serializers.CharField(source='board.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Test
        fields = '__all__'


class TestCommentSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='test.board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='test.board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='test.board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='test.board.classroom.class_name', read_only=True)
    board_id = serializers.IntegerField(source='test.board.id', read_only=True)
    board_name = serializers.CharField(source='test.board.title', read_only=True)
    post_name = serializers.CharField(source='test.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    current_user = serializers.SerializerMethodField(read_only=True)

    def get_current_user(self, request):
        request = self.context.get('request', None)
        return request.user.user_id

    class Meta:
        model = TestComment
        fields = '__all__'


class LectureNoteSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='board.classroom.class_name', read_only=True)
    board_name = serializers.CharField(source='board.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    upload_file = serializers.FileField(required=False, allow_null=True)
    upload_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = LectureNote
        fields = '__all__'


class LectureNoteCommentSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='lecture_note.board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='lecture_note.board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='lecture_note.board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='lecture_note.board.classroom.class_name', read_only=True)
    board_id = serializers.IntegerField(source='lecture_note.board.id', read_only=True)
    board_name = serializers.CharField(source='lecture_note.board.title', read_only=True)
    post_name = serializers.CharField(source='lecture_note.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    current_user = serializers.SerializerMethodField(read_only=True)

    def get_current_user(self, request):
        request = self.context.get('request', None)
        return request.user.user_id

    class Meta:
        model = LectureNoteComment
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='board.classroom.class_name', read_only=True)
    board_name = serializers.CharField(source='board.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    upload_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='question.board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='question.board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='question.board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='question.board.classroom.class_name', read_only=True)
    board_id = serializers.IntegerField(source='question.board.id', read_only=True)
    board_name = serializers.CharField(source='question.board.title', read_only=True)
    post_name = serializers.CharField(source='question.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    current_user = serializers.SerializerMethodField(read_only=True)

    def get_current_user(self, request):
        request = self.context.get('request', None)
        return request.user.user_id

    class Meta:
        model = QuestionComment
        fields = '__all__'


class TestSubmitSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='test.board.classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='test.board.classroom.user.nickname', read_only=True)
    classroom_id = serializers.IntegerField(source='test.board.classroom.id', read_only=True)
    classroom_name = serializers.CharField(source='test.board.classroom.class_name', read_only=True)
    board_id = serializers.IntegerField(source='test.board.id', read_only=True)
    board_name = serializers.CharField(source='test.board.title', read_only=True)
    post_name = serializers.CharField(source='test.title', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = TestSubmit
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    classroom_user_id = serializers.IntegerField(source='classroom.user.id', read_only=True)
    classroom_user_name = serializers.CharField(source='classroom.user.nickname', read_only=True)
    classroom_name = serializers.CharField(source='classroom.class_name', read_only=True)
    user_id = serializers.CharField(source='user.user_id', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'
