from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classroom, Test, TestBoard, LectureNote, LectureNoteBoard, Question, QuestionBoard, Comment, \
    TestSubmit
from .serializers import ClassroomSerializer, TestSerializer, TestBoardSerializer, LectureNoteSerializer, \
    LectureNoteBoardSerializer, QuestionSerializer, QuestionBoardSerializer, CommentSerializer, \
    TestSubmitSerializer


### Classroom 클래스룸
class ClassroomView(APIView):
    def get(self, request):
        queryset = Classroom.objects.all()
        serializer = ClassroomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassroomDetailView(APIView):
    def get(self, request, pk):
        queryset = Classroom.objects.get(pk=pk)
        serializer = ClassroomSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = Classroom.objects.get(pk=pk)
        serializer = ClassroomSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Classroom.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Classroom deleted'}, status=status.HTTP_202_ACCEPTED)


class ClassroomTagView(APIView):
    def get(self, request):
        queryset = Classroom.objects.all()
        tag = request.GET.get('tag', '')
        if tag:
            queryset = queryset.filter(tag__icontains=tag)

        serializer = ClassroomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Classroom 클래스룸


### TestBoard 문제게시판
class TestBoardView(APIView):
    def get(self, request):
        queryset = TestBoard.objects.all()
        serializer = TestBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestBoardSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestBoardDetailView(APIView):
    def get(self, request, pk):
        queryset = TestBoard.objects.get(pk=pk)
        serializer = TestBoardSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = TestBoard.objects.get(pk=pk)
        serializer = TestBoardSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = TestBoard.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'TestBoard deleted'}, status=status.HTTP_202_ACCEPTED)


class TestBoardByClassView(APIView):
    def get(self, request, pk):
        queryset = TestBoard.objects.filter(classroom=pk)
        serializer = TestBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /TestBoard 문제게시판


### Test 문제게시글
class TestView(APIView):
    def get(self, request):
        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetailView(APIView):
    def get(self, request, pk):
        queryset = Test.objects.get(pk=pk)
        serializer = TestSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = Test.objects.get(pk=pk)
        serializer = TestSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Test.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'TestBoard deleted'}, status=status.HTTP_202_ACCEPTED)


class TestByBoardView(APIView):
    def get(self, request, pk):
        queryset = TestBoard.objects.filter(board=pk)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Test 문제게시글


### LectureNoteBoard 강의자료게시판
class LectureNoteBoardView(APIView):
    def get(self, request):
        queryset = LectureNoteBoard.objects.all()
        serializer = LectureNoteBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LectureNoteBoardSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LectureNoteBoardDetailView(APIView):
    def get(self, request, pk):
        queryset = LectureNoteBoard.objects.get(pk=pk)
        serializer = LectureNoteBoardSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = LectureNoteBoard.objects.get(pk=pk)
        serializer = LectureNoteBoardSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = LectureNoteBoard.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'LectureNoteBoard deleted'}, status=status.HTTP_202_ACCEPTED)


class LectureNoteBoardByClassView(APIView):
    def get(self, request, pk):
        queryset = LectureNoteBoard.objects.filter(classroom=pk)
        serializer = LectureNoteBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /LectureNoteBoard 강의자료게시판


### LectureNote 강의자료게시글
class LectureNoteView(APIView):
    def get(self, request):
        queryset = LectureNote.objects.all()
        serializer = LectureNoteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LectureNoteSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LectureNoteDetailView(APIView):
    def get(self, request, pk):
        queryset = LectureNote.objects.get(pk=pk)
        serializer = LectureNoteSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = LectureNote.objects.get(pk=pk)
        serializer = LectureNoteSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = LectureNote.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'LectureNote deleted'}, status=status.HTTP_202_ACCEPTED)


class LectureNoteByBoardView(APIView):
    def get(self, request, pk):
        queryset = TestBoard.objects.filter(board=pk)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /LectureNote 강의자료게시글


### QuestionBoard 질문게시판
class QuestionBoardView(APIView):
    def get(self, request):
        queryset = QuestionBoard.objects.all()
        serializer = QuestionBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionBoardSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionBoardDetailView(APIView):
    def get(self, request, pk):
        queryset = QuestionBoard.objects.get(pk=pk)
        serializer = QuestionBoardSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = QuestionBoard.objects.get(pk=pk)
        serializer = QuestionBoardSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = QuestionBoard.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'QuestionBoard deleted'}, status=status.HTTP_202_ACCEPTED)


class QuestionBoardByClassView(APIView):
    def get(self, request, pk):
        queryset = QuestionBoard.objects.filter(classroom=pk)
        serializer = QuestionBoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /QuestionBoard 질문게시판


### Question 질문게시글
class QuestionView(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    def get(self, request, pk):
        queryset = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Question.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Question deleted'}, status=status.HTTP_202_ACCEPTED)


class QuestionByBoardView(APIView):
    def get(self, request, pk):
        queryset = Question.objects.filter(classroom=pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Question 질문게시글


### Comment 댓글
class CommentView(APIView):
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    def get(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Comment deleted'}, status=status.HTTP_202_ACCEPTED)


class CommentByBoardView(APIView):
    def get(self, request, pk):
        queryset = Comment.objects.filter(classroom=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Comment 댓글


### TestSubmit 문제 답변
class TestSubmitView(APIView):
    def get(self, request):
        queryset = TestSubmit.objects.all()
        serializer = TestSubmitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestSubmitSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestSubmitDetailView(APIView):
    def get(self, request, pk):
        queryset = TestSubmit.objects.get(pk=pk)
        serializer = TestSubmitSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = TestSubmit.objects.get(pk=pk)
        serializer = TestSubmitSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = TestSubmit.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'TestSubmit deleted'}, status=status.HTTP_202_ACCEPTED)


class TestSubmitByTestView(APIView):
    def get(self, request, pk):
        queryset = TestSubmit.objects.filter(test=pk)
        serializer = TestSubmitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /TestSubmit 문제 답변
