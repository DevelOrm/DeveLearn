from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classroom, Test, TestBoard, TestComment, LectureNote, LectureNoteBoard, LectureNoteComment, \
    Question, QuestionBoard, QuestionComment, TestSubmit
from .serializers import ClassroomSerializer, TestSerializer, TestBoardSerializer, TestCommentSerializer, \
    LectureNoteSerializer, LectureNoteBoardSerializer, LectureNoteCommentSerializer, QuestionSerializer, \
    QuestionBoardSerializer, QuestionCommentSerializer, TestSubmitSerializer


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
        tag = request.GET.get('tag')
        print(tag)
        if tag:
            queryset = queryset.filter(tag__icontains=tag)

        serializer = ClassroomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClassroomByTeacherView(APIView):
    def get(self, request, pk):
        queryset = Classroom.objects.filter(user=pk)
        serializer = ClassroomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllBoardByClassView(APIView):
    def get(self, request):
        test_board_queryset = TestBoard.objects.all()
        lecture_note_board_queryset = LectureNoteBoard.objects.all()
        question_board_queryset = QuestionBoard.objects.all()

        classroom = request.GET.get('classroom', '')

        if classroom:
            test_board_queryset = test_board_queryset.filter(classroom=classroom)
            lecture_note_board_queryset = lecture_note_board_queryset.filter(classroom=classroom)
            question_board_queryset = question_board_queryset.filter(classroom=classroom)

        test_board_serializer = TestBoardSerializer(test_board_queryset, many=True)
        lecture_note_board_serializer = LectureNoteBoardSerializer(lecture_note_board_queryset, many=True)
        question_board_serializer = QuestionBoardSerializer(question_board_queryset, many=True)

        context = {
            "test_board": test_board_serializer.data,
            "lecture_note_board": lecture_note_board_serializer.data,
            "question_board": question_board_serializer.data
        }

        return Response(context)
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
        return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)


class TestByBoardView(APIView):
    def get(self, request, pk):
        queryset = Test.objects.filter(board=pk)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Test 문제게시글


### TestComment 문제댓글
class TestCommentView(APIView):
    def get(self, request):
        queryset = TestComment.objects.all()
        serializer = TestCommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestCommentSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestCommentDetailView(APIView):
    def get(self, request, pk):
        queryset = TestComment.objects.get(pk=pk)
        serializer = TestCommentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = TestComment.objects.get(pk=pk)
        serializer = TestCommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = TestComment.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)


class TestCommentByPostView(APIView):
    def get(self, request, pk):
        queryset = TestComment.objects.filter(test=pk)
        serializer = TestCommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /TestComment 문제댓글


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
        queryset = LectureNote.objects.filter(board=pk)
        serializer = LectureNoteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /LectureNote 강의자료게시글


### LectureNoteComment 강의자료댓글
class LectureNoteCommentView(APIView):
    def get(self, request):
        queryset = LectureNoteComment.objects.all()
        serializer = LectureNoteCommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LectureNoteCommentSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LectureNoteCommentDetailView(APIView):
    def get(self, request, pk):
        queryset = LectureNoteComment.objects.get(pk=pk)
        serializer = LectureNoteCommentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = LectureNoteComment.objects.get(pk=pk)
        serializer = LectureNoteCommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = LectureNoteComment.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)


class LectureNoteCommentByPostView(APIView):
    def get(self, request, pk):
        queryset = LectureNoteComment.objects.filter(lecture_note=pk)
        serializer = LectureNoteCommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /LectureNoteComment 강의자료댓글


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
        queryset = Question.objects.filter(board=pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
### /Question 질문게시글


### Comment 댓글
class QuestionCommentView(APIView):
    def get(self, request):
        queryset = QuestionComment.objects.all()
        serializer = QuestionCommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionCommentSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionCommentDetailView(APIView):
    def get(self, request, pk):
        queryset = QuestionComment.objects.get(pk=pk)
        serializer = QuestionCommentSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        queryset = QuestionComment.objects.get(pk=pk)
        serializer = QuestionCommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = QuestionComment.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Comment deleted'}, status=status.HTTP_202_ACCEPTED)


class QuestionCommentByPostView(APIView):
    def get(self, request, pk):
        queryset = QuestionComment.objects.filter(question=pk)
        serializer = QuestionCommentSerializer(queryset, many=True)
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
