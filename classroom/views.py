from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Classroom, Test, TestBoard, TestComment, LectureNote, LectureNoteBoard, LectureNoteComment, \
    Question, QuestionBoard, QuestionComment, TestSubmit, Subscription
from .serializers import ClassroomSerializer, TestSerializer, TestBoardSerializer, TestCommentSerializer, \
    LectureNoteSerializer, LectureNoteBoardSerializer, LectureNoteCommentSerializer, QuestionSerializer, \
    QuestionBoardSerializer, QuestionCommentSerializer, TestSubmitSerializer, SubscriptionSerializer


### Classroom 클래스룸
class ClassroomView(APIView):
    def get(self, request):
        try:
            queryset = Classroom.objects.all()
            serializer = ClassroomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        if request.user.is_authenticated:
            context = {
                'user': request.user.pk,
                'class_name': request.data['class_name'],
                'class_info': request.data['class_info'],
                'tag': request.data['tag']
            }
            try:
                serializer = ClassroomSerializer(data=context)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "need to login"}, status=status.HTTP_403_FORBIDDEN)


class ClassroomDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            print(request.user)
            print(queryset.user)
            serializer = ClassroomSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'class_name': request.data['class_name'],
                'class_info': request.data['class_info'],
                'tag': request.data['tag']
            }
            serializer = ClassroomSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Classroom deleted'}, status=status.HTTP_202_ACCEPTED)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClassroomTagView(APIView):
    def get(self, request):
        try:
            queryset = Classroom.objects.all()
            tag = request.GET.get('tag')
            if tag:
                queryset = queryset.filter(tag__icontains=tag)
            serializer = ClassroomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClassroomByTeacherView(APIView):
    def get(self, request, pk):
        try:
            queryset = Classroom.objects.filter(user=pk)
            serializer = ClassroomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AllBoardByClassView(APIView):
    def get(self, request):
        try:
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
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Classroom 클래스룸


### Subscription 구독정보
class SubscriptionView(APIView):
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.filter(classroom=pk)
            serializer = SubscriptionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            context = {
                "user": request.user.pk,
                "subscription_memo": request.data['subscription_memo'],
                "classroom": pk
            }
            serializer = SubscriptionSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            serializer = SubscriptionSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'subscription_memo': request.data['subscription_memo'],
                'classroom': queryset.classroom.pk
            }
            print(queryset.user.pk)
            serializer = SubscriptionSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Subscription deleted'}, status=status.HTTP_202_ACCEPTED)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionByUserView(APIView):
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.filter(user=pk)
            serializer = SubscriptionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Subscription 구독정보


### TestBoard 문제게시판
class TestBoardView(APIView):
    def get(self, request):
        try:
            queryset = TestBoard.objects.all()
            serializer = TestBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'classroom': request.data['classroom'],
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = TestBoardSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestBoardDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestBoard.objects.get(pk=pk)
            serializer = TestBoardSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TestBoard.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = TestBoard.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'classroom': queryset.classroom.pk,
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = TestBoardSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TestBoard.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = TestBoard.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'TestBoard deleted'}, status=status.HTTP_202_ACCEPTED)
        except TestBoard.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestBoardByClassView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestBoard.objects.filter(classroom=pk)
            serializer = TestBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /TestBoard 문제게시판


### Test 문제게시글
class TestView(APIView):
    def get(self, request):
        try:
            queryset = Test.objects.all()
            serializer = TestSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'board': request.data['board'],
                'title': request.data['title'],
                'content': request.data['content'],
                'solution': request.data['solution'],
                'auto_score': request.data['auto_score']
            }
            serializer = TestSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            serializer = TestSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'board': queryset.board.pk,
                'title': request.data['title'],
                'content': request.data['content'],
                'solution': request.data['solution'],
                'auto_score': request.data['auto_score']
            }
            serializer = TestSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestByBoardView(APIView):
    def get(self, request, pk):
        try:
            queryset = Test.objects.filter(board=pk)
            serializer = TestSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Test 문제게시글


### TestComment 문제댓글
class TestCommentView(APIView):
    def get(self, request):
        try:
            queryset = TestComment.objects.all()
            serializer = TestCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'test': request.data['test'],
                'content': request.data['content']
            }
            serializer = TestCommentSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestCommentDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            serializer = TestCommentSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'test': queryset.test.pk,
                'content': request.data['content']
            }
            serializer = TestCommentSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'TestComment deleted'}, status=status.HTTP_202_ACCEPTED)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestCommentByPostView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestComment.objects.filter(test=pk)
            serializer = TestCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /TestComment 문제댓글


### LectureNoteBoard 강의자료게시판
class LectureNoteBoardView(APIView):
    def get(self, request):
        try:
            queryset = LectureNoteBoard.objects.all()
            serializer = LectureNoteBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'classroom': request.data['classroom'],
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = LectureNoteBoardSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteBoardDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNoteBoard.objects.get(pk=pk)
            serializer = LectureNoteBoardSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LectureNoteBoard.DoesNotExist:
            return Response({"error": "LectureNoteBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = LectureNoteBoard.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'classroom': queryset.classroom.pk,
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = LectureNoteBoardSerializer(queryset, context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LectureNoteBoard.DoesNotExist:
            return Response({"error": "LectureNoteBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = LectureNoteBoard.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'LectureNoteBoard deleted'}, status=status.HTTP_202_ACCEPTED)
        except LectureNoteBoard.DoesNotExist:
            return Response({"error": "LectureNoteBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteBoardByClassView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNoteBoard.objects.filter(classroom=pk)
            serializer = LectureNoteBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LectureNoteBoard.DoesNotExist:
            return Response({"error": "LectureNoteBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /LectureNoteBoard 강의자료게시판


### LectureNote 강의자료게시글
class LectureNoteView(APIView):
    def get(self, request):
        try:
            queryset = LectureNote.objects.all()
            serializer = LectureNoteSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'board': request.data['board'],
                'title': request.data['title'],
                'content': request.data['content'],
                'upload_file': request.data['upload_file'],
                'upload_image': request.data['upload_image']
            }
            serializer = LectureNoteSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            serializer = LectureNoteSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'board': queryset.board.pk,
                'title': request.data['title'],
                'content': request.data['content'],
                'upload_file': request.data['upload_file'],
                'upload_image': request.data['upload_image']
            }
            serializer = LectureNoteSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'LectureNote deleted'}, status=status.HTTP_202_ACCEPTED)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteByBoardView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNote.objects.filter(board=pk)
            serializer = LectureNoteSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /LectureNote 강의자료게시글


### LectureNoteComment 강의자료댓글
class LectureNoteCommentView(APIView):
    def get(self, request):
        try:
            queryset = LectureNoteComment.objects.all()
            serializer = LectureNoteCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'lecture_note': request.data['lecture_note'],
                'content': request.data['content']
            }
            serializer = LectureNoteCommentSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteCommentDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            serializer = LectureNoteCommentSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'lecture_note': queryset.lecture_note.pk,
                'content': request.data['content']
            }
            serializer = LectureNoteCommentSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteCommentByPostView(APIView):
    def get(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.filter(lecture_note=pk)
            serializer = LectureNoteCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /LectureNoteComment 강의자료댓글


### QuestionBoard 질문게시판
class QuestionBoardView(APIView):
    def get(self, request):
        try:
            queryset = QuestionBoard.objects.all()
            serializer = QuestionBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'classroom': request.data['classroom'],
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = QuestionBoardSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionBoardDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = QuestionBoard.objects.get(pk=pk)
            serializer = QuestionBoardSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except QuestionBoard.DoesNotExist:
            return Response({"error": "QuestionBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = QuestionBoard.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'classroom': queryset.classroom.pk,
                'title': request.data['title'],
                'content': request.data['content']
            }
            serializer = QuestionBoardSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except QuestionBoard.DoesNotExist:
            return Response({"error": "QuestionBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = QuestionBoard.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'QuestionBoard deleted'}, status=status.HTTP_202_ACCEPTED)
        except QuestionBoard.DoesNotExist:
            return Response({"error": "QuestionBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionBoardByClassView(APIView):
    def get(self, request, pk):
        try:
            queryset = QuestionBoard.objects.filter(classroom=pk)
            serializer = QuestionBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /QuestionBoard 질문게시판


### Question 질문게시글
class QuestionView(APIView):
    def get(self, request):
        try:
            queryset = Question.objects.all()
            serializer = QuestionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'board': queryset.board.pk,
                'title': request.data['title'],
                'content': request.data['content'],
                'upload_image': request.data['upload_image']
            }
            serializer = QuestionSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Question deleted'}, status=status.HTTP_202_ACCEPTED)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionByBoardView(APIView):
    def get(self, request, pk):
        try:
            queryset = Question.objects.filter(board=pk)
            serializer = QuestionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Question 질문게시글


### Comment 댓글
class QuestionCommentView(APIView):
    def get(self, request):
        try:
            queryset = QuestionComment.objects.all()
            serializer = QuestionCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            context = {
                'user': request.user.pk,
                'question': request.data['question'],
                'content': request.data['content']
            }
            serializer = QuestionCommentSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionCommentDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            serializer = QuestionCommentSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            context = {
                'user': queryset.user.pk,
                'question': queryset.question.pk,
                'content': request.data['content']
            }
            serializer = QuestionCommentSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'Comment deleted'}, status=status.HTTP_202_ACCEPTED)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionCommentByPostView(APIView):
    def get(self, request, pk):
        try:
            queryset = QuestionComment.objects.filter(question=pk)
            serializer = QuestionCommentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Comment 댓글


### TestSubmit 문제 답변
class TestSubmitView(APIView):
    def get(self, request):
        try:
            queryset = TestSubmit.objects.all()
            serializer = TestSubmitSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            test_pk = request.data['test']
            test_obj = Test.objects.get(pk=test_pk)
            solution = test_obj.solution
            user_answer = request.data['user_answer']

            if test_obj.auto_score:
                answer_status = user_answer in solution
            else:
                answer_status = None

            context = {
                'user': request.user.pk,
                'test': test_pk,
                'user_answer': user_answer,
                'answer_status': answer_status,
            }

            serializer = TestSubmitSerializer(data=context)
            if serializer.is_valid():
                queryset = serializer.save(answer_status=answer_status)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitDetailView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestSubmit.objects.get(pk=pk)
            serializer = TestSubmitSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            test_pk = request.data['test']
            test_obj = Test.objects.get(pk=test_pk)
            solution = test_obj.solution
            user_answer = request.data['user_answer']

            if test_obj.auto_score:
                answer_status = user_answer in solution
            else:
                try:
                    answer_status = request.data['answer_status']
                except:
                    answer_status = None

            queryset = TestSubmit.objects.get(pk=pk)

            context = {
                'user': queryset.user.pk,
                'test': test_pk,
                'user_answer': user_answer,
                'answer_status': answer_status
            }

            serializer = TestSubmitSerializer(queryset, data=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            queryset = TestSubmit.objects.get(pk=pk)
            queryset.delete()
            return Response({'message': 'TestSubmit deleted'}, status=status.HTTP_202_ACCEPTED)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitByTestView(APIView):
    def get(self, request, pk):
        try:
            queryset = TestSubmit.objects.filter(test=pk)
            serializer = TestSubmitSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitByTestUserView(APIView):
    def get(self, request, test_pk, user_pk):
        try:
            queryset = TestSubmit.objects.filter(test=test_pk, user=user_pk)
            serializer = TestSubmitSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /TestSubmit 문제 답변
