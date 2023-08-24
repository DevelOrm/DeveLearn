from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classroom, Test, TestBoard, TestComment, LectureNote, LectureNoteBoard, LectureNoteComment, \
    Question, QuestionBoard, QuestionComment, TestSubmit
from .serializers import ClassroomSerializer, TestSerializer, TestBoardSerializer, TestCommentSerializer, \
    LectureNoteSerializer, LectureNoteBoardSerializer, LectureNoteCommentSerializer, QuestionSerializer, \
    QuestionBoardSerializer, QuestionCommentSerializer, TestSubmitSerializer

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view, extend_schema, OpenApiTypes
from rest_framework.decorators import action


### Classroom 클래스룸
class ClassroomView(APIView):
    @extend_schema(
        # responses={status.HTTP_200_OK: OpenApiExample("Classroom list example", response_serializer=ClassroomSerializer)},
        summary="클래스룸 전체 리스트 보기", # summary : 해당 method 요약
        description="클래스룸 전체 리스트 보기", # description: 해당 method 설명
        tags=["Classroom"], # tags : 문서상 보여줄 묶음의 단위
        responses=ClassroomSerializer,
        methods=["GET", "POST", "DELETE", "PUT", "PATCH"],
        # auth=["string"],
        # operation_id: Optional[str] = None,
	    # parameters: Optional[List[Union[OpenApiParameter, _SerializerType]]] = None,
		# request: Any = empty,
		# auth: Optional[List[str]] = None,
		# deprecated: Optional[bool] = None,
		# exclude: bool = False,
		# operation: Optional[Dict] = None,
		# methods: Optional[List[str]] = None,
		# versions: Optional[List[str]] = None,
		# examples: Optional[List[OpenApiExample]] = None,

        # operation_id : 자동으로 설정되는 id 값, 대체로 수동할당하여 쓰진 않음
		# parameters : 해당 path로 받기로 예상된 파라미터 값 (Serializer or OpenApiParameter 사용)
		# request : 요청시 전달될 content의 형태
		# responses : 응답시 전달될 content의 형태
		# auth : 해당 method에 접근하기 위한 인증방법
		# description: 해당 method 설명
		# summary : 해당 method 요약
		# deprecated : 해당 method 사용여부 
		# tags : 문서상 보여줄 묶음의 단위
		# exclude : 문서에서 제외여부  
		# operation : ??? json -> yaml 하기위한 dictionary??? 
		# methods : 요청 받을 Http method 목록
		# versions : 문서화 할때 사용할 openAPI 버전
		# examples : 요청/응답에 대한 예시
        
        examples=[
            OpenApiExample(
                response_only=True,
                summary="summary example",
                name="success_example",
                value={
                    "id": "sample",
                    "class_name": "sample",
                    "class_info": "sample",
                    "created_at": "sample",
                    "tag": "sample",
                },
            ),
        ],
        parameters=[
            OpenApiParameter(
                name="path_parameter",
                type=str,
                location=OpenApiParameter.PATH,
                description="아이디 입니다.",
                required=True,
            ),
            OpenApiParameter(
                name="text_parameter",
                type=str,
                description="text_param 입니다.",
                required=False,
            ),
            OpenApiParameter(
                name="select_parameter",
                type=str,
                description="first_param 입니다.",
				
                #enum : 받을 수 있는 값을 제한함
                enum=['선택1', '선택2', '선택3'], 
                examples=[
                    OpenApiExample(
                        name="Select Parameter Example",
                        summary="요약1",
                        description="설명글은 길게 작성합니다",
                        value="선택1",
                    ),
                    OpenApiExample(
                        "Select Parameter Example2",
                        summary="요약2",
                        description="두번째 설명글은 더 길게 작성합니다",
                        value="선택4",
                    ),
                ],
            ),
            OpenApiParameter(
                name="date_parameter",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="date filter",
                examples=[
                    OpenApiExample(
                        name="이것은 Query Parameter Example입니다.",
                        summary="요약입니다",
                        description="설명글은 길게 작성합니다",
                        value="1991-03-02",
                    ),
                    OpenApiExample(
                        name="이것은 Query Parameter Example2입니다.",
                        summary="두번째 요약입니다",
                        description="두번째 설명글은 더 길게 작성합니다",
                        value="1993-08-30",
                    ),
                ],
            ),
        ],
    )
    def get(self, request):
        try:
            queryset = Classroom.objects.all()
            serializer = ClassroomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        # responses={
        #     status.HTTP_201_CREATED: OpenApiExample("Classroom created example", response_serializer=ClassroomSerializer),
        #     status.HTTP_400_BAD_REQUEST: "Bad request"
        # },
        summary="신규 클래스룸 생성",
        description="신규 클래스룸 생성",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def post(self, request):
        try:
            serializer = ClassroomSerializer(data=request.data)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClassroomDetailView(APIView):
    @extend_schema(
        request=ClassroomSerializer,
        # responses={
        #     status.HTTP_201_CREATED: OpenApiExample("Classroom created example", response_serializer=ClassroomSerializer),
        #     status.HTTP_400_BAD_REQUEST: "Bad request"
        # },
        summary="임시",
        description="임시",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        # responses={
        #     status.HTTP_201_CREATED: OpenApiExample("Classroom created example", response_serializer=ClassroomSerializer),
        #     status.HTTP_400_BAD_REQUEST: "Bad request"
        # },
        summary="임시",
        description="임시",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def post(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        # responses={
        #     status.HTTP_201_CREATED: OpenApiExample("Classroom created example", response_serializer=ClassroomSerializer),
        #     status.HTTP_400_BAD_REQUEST: "Bad request"
        # },
        summary="임시",
        description="임시",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
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
    @extend_schema(
        request=ClassroomSerializer,
        # responses={
        #     status.HTTP_201_CREATED: OpenApiExample("Classroom created example", response_serializer=ClassroomSerializer),
        #     status.HTTP_400_BAD_REQUEST: "Bad request"
        # },
        summary="임시",
        description="임시",
        tags=["Classroom-Tag"],
        responses=ClassroomSerializer,
    )
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
    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Classroom.objects.filter(user=pk)
            serializer = ClassroomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AllBoardByClassView(APIView):
    @extend_schema(
        request=ClassroomSerializer,
        summary="클래스 내 게시판 보기",
        description="임시",
        tags=["Classroom-Board"],
        responses=ClassroomSerializer,
    )
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


### TestBoard 문제게시판
class TestBoardView(APIView):
    @extend_schema(
        request=ClassroomSerializer,
        summary="문제 게시판 보기",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request):
        try:
            queryset = TestBoard.objects.all()
            serializer = TestBoardSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="문제 게시판 생성",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def post(self, request):
        try:
            serializer = TestBoardSerializer(data=request.data)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestBoardDetailView(APIView):
    @extend_schema(
        request=ClassroomSerializer,
        summary="문제 게시판 상세보기",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = TestBoard.objects.get(pk=pk)
            serializer = TestBoardSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TestBoard.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="문제 게시판 생성",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def post(self, request, pk):
        try:
            queryset = TestBoard.objects.get(pk=pk)
            serializer = TestBoardSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TestBoard.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="문제 게시판 삭제",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
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
    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
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
    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request):
        try:
            queryset = Test.objects.all()
            serializer = TestSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def post(self, request):
        try:
            serializer = TestSerializer(data=request.data)
            if serializer.is_valid():
                queryset = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestDetailView(APIView):
    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            serializer = TestSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def post(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            serializer = TestSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
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
    @extend_schema(
        request=ClassroomSerializer,
        summary="임시",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Test.objects.filter(board=pk)
            serializer = TestSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
### /Test 문제게시글

## classroom/test까지 spectacular 1차 적용 - depth 구분 범위 재검토 필요
## ==================================================================================

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
            serializer = TestCommentSerializer(data=request.data)
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
            serializer = TestCommentSerializer(queryset, data=request.data)
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
            serializer = LectureNoteBoardSerializer(data=request.data)
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
            serializer = LectureNoteBoardSerializer(queryset, data=request.data)
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
            serializer = LectureNoteSerializer(data=request.data)
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
            serializer = LectureNoteSerializer(queryset, data=request.data)
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
            serializer = LectureNoteCommentSerializer(data=request.data)
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
            serializer = LectureNoteCommentSerializer(queryset, data=request.data)
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
            serializer = QuestionBoardSerializer(data=request.data)
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
            serializer = QuestionBoardSerializer(queryset, data=request.data)
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
            serializer = QuestionSerializer(queryset, data=request.data)
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
            serializer = QuestionCommentSerializer(data=request.data)
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
            serializer = QuestionCommentSerializer(queryset, data=request.data)
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
            serializer = TestSubmitSerializer(data=request.data)
            if serializer.is_valid():
                queryset = serializer.save()
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
            queryset = TestSubmit.objects.get(pk=pk)
            serializer = TestSubmitSerializer(queryset, data=request.data)
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
