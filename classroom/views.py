from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Classroom, Test, Board, TestComment, LectureNote, LectureNoteComment, Question, QuestionComment, \
    TestSubmit, Subscription
from .serializers import ClassroomSerializer, TestSerializer, BoardSerializer, TestCommentSerializer, \
    LectureNoteSerializer, LectureNoteCommentSerializer, QuestionSerializer, QuestionCommentSerializer, \
    TestSubmitSerializer, SubscriptionSerializer


class ClassroomPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page'


class PostPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class CommentPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'


class TestSubmitPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


###################
# schema-option 정리
# responses=ClassroomSerializer,
# methods=["GET", "POST", "DELETE", "PUT", "PATCH"],
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
####################

# Classroom 클래스룸


class ClassroomView(APIView):
    paginator = ClassroomPagination()

    @extend_schema(
        summary="클래스 목록 조회",  # summary : 해당 method 요약
        description="클래스 목록 조회",  # description: 해당 method 설명
        tags=["Classroom"],  # tags : 문서상 보여줄 묶음의 단위
        responses=ClassroomSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                summary="summary example",
                name="success_example",
                value={
                    "id": 1,
                    "created_at": "2023-08-24T10:01:38",
                    "updated_at": "2023-08-28T10:01:28",
                    "class_name": "class500",
                    "class_info": "info500",
                    "tag": [
                        "#500"
                    ]
                },
            ),
        ],

        # parameters=[
        #     OpenApiParameter(
        #         name="path_parameter",
        #         type=str,
        #         location=OpenApiParameter.PATH,
        #         description="아이디 입니다.",
        #         required=True,
        #     ),
        #     OpenApiParameter(
        #         name="text_parameter",
        #         type=str,
        #         description="text_param 입니다.",
        #         required=False,
        #     ),
        #     OpenApiParameter(
        #         name="select_parameter",
        #         type=str,
        #         description="first_param 입니다.",

        #         #enum : 받을 수 있는 값을 제한함
        #         enum=['선택1', '선택2', '선택3'],
        #         examples=[
        #             OpenApiExample(
        #                 name="Select Parameter Example",
        #                 summary="요약1",
        #                 description="설명글은 길게 작성합니다",
        #                 value="선택1",
        #             ),
        #             OpenApiExample(
        #                 "Select Parameter Example2",
        #                 summary="요약2",
        #                 description="두번째 설명글은 더 길게 작성합니다",
        #                 value="선택4",
        #             ),
        #         ],
        #     ),
        #     OpenApiParameter(
        #         name="date_parameter",
        #         type=OpenApiTypes.DATE,
        #         location=OpenApiParameter.QUERY,
        #         description="date filter",
        #         examples=[
        #             OpenApiExample(
        #                 name="이것은 Query Parameter Example입니다.",
        #                 summary="요약입니다",
        #                 description="설명글은 길게 작성합니다",
        #                 value="1991-03-02",
        #             ),
        #             OpenApiExample(
        #                 name="이것은 Query Parameter Example2입니다.",
        #                 summary="두번째 요약입니다",
        #                 description="두번째 설명글은 더 길게 작성합니다",
        #                 value="1993-08-30",
        #             ),
        #         ],
        #     ),
        # ],
    )
    def get(self, request):
        try:
            queryset = Classroom.objects.all()
            result_page = self.paginator.paginate_queryset(queryset, request)
            serializer = ClassroomSerializer(result_page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=ClassroomSerializer,
        summary="클래스 생성",
        description="클래스 생성",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def post(self, request):
        if request.user.is_authenticated and request.user.is_teacher:
            user = request.user
            request.data['user'] = user.pk
            try:
                serializer = ClassroomSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)


class ClassroomDetailView(APIView):
    @extend_schema(
        summary="클래스 상세 조회",
        description="클래스 상세 조회",
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
        summary="클래스 수정",
        description="클래스 수정",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = ClassroomSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="클래스 삭제",
        description="클래스 삭제",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = Classroom.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Classroom deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClassroomTagView(APIView):
    paginator = ClassroomPagination()

    @extend_schema(
        summary="태그별 클래스 조회",
        description="태그별 클래스 조회",
        tags=["Classroom-Tag"],
        responses=ClassroomSerializer,
    )
    def get(self, request):
        try:
            queryset = Classroom.objects.all()
            tag = request.GET.get('tag')
            if tag:
                queryset = queryset.filter(tag__icontains=tag)
            result_page = self.paginator.paginate_queryset(queryset, request)
            serializer = ClassroomSerializer(result_page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClassroomByTeacherView(APIView):
    paginator = ClassroomPagination()

    @extend_schema(
        summary="교사별 클래스 조회",
        description="교사별 클래스 조회",
        tags=["Classroom"],
        responses=ClassroomSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Classroom.objects.filter(user=pk)
            result_page = self.paginator.paginate_queryset(queryset, request)
            serializer = ClassroomSerializer(result_page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Subscription 구독정보
class SubscriptionView(APIView):
    @extend_schema(
        summary="클래스 구독 정보 조회",
        description="클래스 구독 정보 조회",
        tags=["Classroom-Subscription"],
        responses=SubscriptionSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.filter(classroom=pk)
            serializer = SubscriptionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="클래스 구독 정보 생성",
        description="클래스 구독 정보 생성",
        tags=["Classroom-Subscription"],
        request=SubscriptionSerializer,    
        responses=SubscriptionSerializer,
    )
    def post(self, request, pk):
        try:
            if request.user.is_authenticated:
                user = request.user
                request.data['user'] = user.pk
                request.data['classroom'] = pk
                serializer = SubscriptionSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionDetailView(APIView):
    @extend_schema(
        summary="클래스 구독 정보 상세 조회",
        description="클래스 구독 정보 상세 조회",
        tags=["Classroom-Subscription"],
        responses=SubscriptionSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = SubscriptionSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
    @extend_schema(
        summary="클래스 구독 정보 수정",
        description="클래스 구독 정보 수정",
        tags=["Classroom-Subscription"],
        request=SubscriptionSerializer,    
        responses=SubscriptionSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = SubscriptionSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="클래스 구독 정보 삭제",
        description="클래스 구독 정보 삭제",
        tags=["Classroom-Subscription"],
        request=SubscriptionSerializer,    
        responses=SubscriptionSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = Subscription.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Subscription deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionByUserView(APIView):
    @extend_schema(
        summary="사용자별 구독 정보 조회",
        description="사용자별 구독 정보 조회",
        tags=["Classroom-Subscription"],
        responses=SubscriptionSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Subscription.objects.filter(user=pk)
            if request.user.is_authenticated and request.user.pk == pk:
                serializer = SubscriptionSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /Subscription 구독정보


# Board 문제게시판
class BoardView(APIView):
    @extend_schema(
        summary="게시판 조회",
        description="게시판 조회",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def get(self, request):
        try:
            queryset = Board.objects.all()
            if request.user.is_authenticated:
                serializer = BoardSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=BoardSerializer,
        summary="게시판 생성",
        description="게시판 생성",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated and request.user.is_teacher:
                user = request.user
                request.data['user'] = user.pk
                serializer = BoardSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BoardDetailView(APIView):
    @extend_schema(
        summary="게시판 조회",
        description="",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Board.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = BoardSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Board.DoesNotExist:
            return Response({"error": "TestBoard not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=BoardSerializer,
        summary="게시판 생성",
        description="임시",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = Board.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = BoardSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Board.DoesNotExist:
            return Response({"error": "Board not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="게시판 삭제",
        description="임시",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = Board.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Board deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Board.DoesNotExist:
            return Response({"error": "Board not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BoardByClassView(APIView):
    @extend_schema(
        summary="클래스별 게시판 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=BoardSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Board.objects.filter(classroom=pk)
            if request.user.is_authenticated:
                serializer = BoardSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /Board 게시판


# Test 문제게시글
class TestView(APIView):
    paginator = PostPagination()

    @extend_schema(
        summary="문제 게시글 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def get(self, request):
        try:
            queryset = Test.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = TestSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=TestSerializer,
        summary="문제 게시글 생성",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                board_pk = request.data['board']
                board_queryset = Board.objects.get(pk=board_pk)
                if board_queryset.board_type == "test":
                    user = request.user
                    request.data['user'] = user.pk
                    request.data['board'] = board_pk
                    serializer = TestSerializer(data=request.data)
                    if serializer.is_valid():
                        queryset = serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({"error": "Select the correct board"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestDetailView(APIView):
    @extend_schema(
        summary="문제 게시글 상세 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = TestSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=TestSerializer,
        summary="문제 게시글 생성",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = TestSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="문제 게시글 삭제",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = Test.objects.get(pk=pk)
            if request.user.is_authenticated:
                if request.user.is_authenticated and request.user == queryset.user:
                    queryset.delete()
                    return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)
                return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Test.DoesNotExist:
            return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestByBoardView(APIView):
    paginator = PostPagination()

    @extend_schema(
        summary="게시판별 게시글 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Test.objects.filter(board=pk)
            if request.user.is_authenticated:
                if request.user.is_authenticated:
                    result_page = self.paginator.paginate_queryset(queryset, request)
                    serializer = TestSerializer(result_page, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /Test 문제게시글

# classroom/test까지 spectacular 1차 적용 - depth 구분 범위 재검토 필요
# ==================================================================================


# TestComment 문제댓글
class TestCommentView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="문제 게시글 댓글 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=ClassroomSerializer,
    )
    def get(self, request):
        try:
            queryset = TestComment.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = TestCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=TestCommentSerializer,
        responses=TestCommentSerializer,
        summary="문제 게시글 댓글 작성",
        description="임시",
        tags=["Classroom-Test"],
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                user = request.user
                request.data['user'] = user.pk
                serializer = TestCommentSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestCommentDetailView(APIView):
    @extend_schema(
        summary="문제 게시글 댓글 상세 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = TestCommentSerializer(queryset, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="문제 게시글 댓글 수정",
        description="임시",
        tags=["Classroom-Test"],
        request=TestCommentSerializer,
        responses=TestCommentSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = TestCommentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="문제 게시글 댓글 삭제",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestCommentSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = TestComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'TestComment deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestComment.DoesNotExist:
            return Response({"error": "TestComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestCommentByPostView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="게시글별 댓글 조회",
        description="임시",
        tags=["Classroom-Test"],
        responses=TestCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = TestComment.objects.filter(test=pk)
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = TestCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /TestComment 문제댓글


# LectureNote 강의자료게시글
class LectureNoteView(APIView):
    paginator = PostPagination()

    @extend_schema(
        summary="강의자료 게시글 전체 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteSerializer,
    )
    def get(self, request):
        try:
            queryset = LectureNote.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = LectureNoteSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 생성",
        description="임시",
        tags=["Classroom-LectureNote"],
        request=LectureNoteSerializer,
        responses=LectureNoteSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                board_pk = request.data['board']
                board_queryset = Board.objects.get(pk=board_pk)
                if board_queryset.board_type == "lecture_note":
                    user = request.user
                    request.data['user'] = user.pk
                    request.data['board'] = board_pk
                    serializer = LectureNoteSerializer(data=request.data)
                    if serializer.is_valid():
                        queryset = serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({"error": "Select the correct board"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteDetailView(APIView):
    @extend_schema(
        summary="강의자료 게시글 상세 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = LectureNoteSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 생성",
        description="임시",
        tags=["Classroom-LectureNote"],
        request=LectureNoteSerializer,
        responses=LectureNoteSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = LectureNoteSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 삭제",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = LectureNote.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'LectureNote deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNote.DoesNotExist:
            return Response({"error": "LectureNote not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteByBoardView(APIView):
    paginator = PostPagination()

    @extend_schema(
        summary="게시판별 게시글 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = LectureNote.objects.filter(board=pk)
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = LectureNoteSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /LectureNote 강의자료게시글


# LectureNoteComment 강의자료댓글
class LectureNoteCommentView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="강의자료 게시글 댓글 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteCommentSerializer,
    )
    def get(self, request):
        try:
            queryset = LectureNoteComment.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = LectureNoteCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 댓글 작성",
        description="임시",
        tags=["Classroom-LectureNote"],
        request=LectureNoteCommentSerializer,
        responses=LectureNoteCommentSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                user = request.user
                request.data['user'] = user.pk
                serializer = LectureNoteCommentSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteCommentDetailView(APIView):
    @extend_schema(
        summary="강의자료 게시글 댓글 상세 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = LectureNoteCommentSerializer(queryset, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 댓글 수정",
        description="임시",
        tags=["Classroom-LectureNote"],
        request=LectureNoteCommentSerializer,
        responses=LectureNoteCommentSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = LectureNoteCommentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="강의자료 게시글 댓글 삭제",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteCommentSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Test deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except LectureNoteComment.DoesNotExist:
            return Response({"error": "LectureNoteComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LectureNoteCommentByPostView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="강의자료 게시글별 댓글 조회",
        description="임시",
        tags=["Classroom-LectureNote"],
        responses=LectureNoteCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = LectureNoteComment.objects.filter(lecture_note=pk)
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = LectureNoteCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /LectureNoteComment 강의자료댓글


# Question 질문게시글
class QuestionView(APIView):

    paginator = PostPagination()

    @extend_schema(
        summary="질문 게시글 전체 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionSerializer,
    )
    def get(self, request):
        try:
            queryset = Question.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = QuestionSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 생성",
        description="임시",
        tags=["Classroom-Question"],
        request=QuestionSerializer,
        responses=QuestionSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                board_pk = request.data['board']
                board_queryset = Board.objects.get(pk=board_pk)
                if board_queryset.board_type == "question":
                    user = request.user
                    request.data['user'] = user.pk
                    serializer = QuestionSerializer(data=request.data)
                    if serializer.is_valid():
                        queryset = serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({"error": "Select the correct board"}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionDetailView(APIView):
    @extend_schema(
        summary="질문 게시글 상세 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = QuestionSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 수정",
        description="임시",
        tags=["Classroom-Question"],
        request=QuestionSerializer,
        responses=QuestionSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                serializer = QuestionSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 삭제",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Question deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionByBoardView(APIView):
    paginator = PostPagination()

    @extend_schema(
        summary="게시판별 게시글 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = Question.objects.filter(board=pk)
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = QuestionSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /Question 질문게시글


# Comment 댓글
class QuestionCommentView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="질문 게시글 댓글 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionCommentSerializer,
    )
    def get(self, request):
        try:
            queryset = QuestionComment.objects.all()
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = QuestionCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 댓글 작성",
        description="임시",
        tags=["Classroom-Question"],
        request=QuestionCommentSerializer,
        responses=QuestionCommentSerializer,
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                user = request.user
                request.data['user'] = user.pk
                serializer = QuestionCommentSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionCommentDetailView(APIView):
    @extend_schema(
        summary="질문 게시글 댓글 상세 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            if request.user.is_authenticated:
                serializer = QuestionCommentSerializer(queryset, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 댓글 수정",
        description="임시",
        tags=["Classroom-Question"],
        request=QuestionCommentSerializer,
        responses=QuestionCommentSerializer,
    )
    def put(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                user = request.user
                request.data['user'] = user.pk
                serializer = QuestionCommentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="질문 게시글 댓글 삭제",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionCommentSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = QuestionComment.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'Comment deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except QuestionComment.DoesNotExist:
            return Response({"error": "QuestionComment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionCommentByPostView(APIView):
    paginator = CommentPagination()

    @extend_schema(
        summary="게시글별 댓글 조회",
        description="임시",
        tags=["Classroom-Question"],
        responses=QuestionCommentSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = QuestionComment.objects.filter(question=pk)
            if request.user.is_authenticated:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = QuestionCommentSerializer(result_page, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /Comment 댓글


# TestSubmit 문제 답변
class TestSubmitView(APIView):
    paginator = TestSubmitPagination()

    @extend_schema(
        summary="문제 답변 조회",
        description="임시",
        tags=["Classroom-TestSubmit"],
        responses=TestSubmitSerializer,
    )
    def get(self, request):
        try:
            queryset = TestSubmit.objects.all()
            if request.user.is_authenticated and request.user.is_teacher:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = TestSubmitSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="문제 답변 제출",
        description="임시",
        tags=["Classroom-TestSubmit"],
        request=TestSubmitSerializer,
        responses=TestSubmitSerializer,
    )
    def post(self, request):
        try:
            test_pk = request.data['test']
            test_obj = Test.objects.get(pk=test_pk)
            if request.user.is_authenticated:
                solution = test_obj.solution
                user_answer = request.data['user_answer']

                if test_obj.auto_score:
                    answer_status = user_answer in solution
                else:
                    answer_status = None

                user = request.user
                request.data['user'] = user.pk
                request.data['answer_status'] = answer_status

                serializer = TestSubmitSerializer(data=request.data)
                if serializer.is_valid():
                    queryset = serializer.save(answer_status=answer_status)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitDetailView(APIView):
    @extend_schema(
        summary="제출한 문제 답변 상세 조회",
        description="임시",
        tags=["Classroom-TestSubmit"],
        responses=TestSubmitSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = TestSubmit.objects.get(pk=pk)
            if request.user.is_authenticated and (request.user.is_teacher or request.user == queryset.user):
                serializer = TestSubmitSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="제출한 문제 답변 수정",
        description="임시",
        tags=["Classroom-TestSubmit"],
        request=TestSubmitSerializer,
        responses=TestSubmitSerializer,
    )
    def put(self, request, pk):
        try:
            test_obj = Test.objects.get(pk=pk)
            if request.user.is_authenticated and (request.user.is_teacher or request.user == test_obj.user):
                solution = test_obj.solution
                user_answer = request.data['user_answer']

                if test_obj.auto_score:
                    answer_status = user_answer in solution
                else:
                    try:
                        answer_status = request.data['answer_status']
                    except:
                        answer_status = None

                request.data['answer_status'] = answer_status

                queryset = TestSubmit.objects.get(pk=pk)
                serializer = TestSubmitSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="제출한 문제 답변 삭제",
        description="임시",
        tags=["Classroom-TestSubmit"],
        responses=TestSubmitSerializer,
    )
    def delete(self, request, pk):
        try:
            queryset = TestSubmit.objects.get(pk=pk)
            if request.user.is_authenticated and request.user == queryset.user:
                queryset.delete()
                return Response({'message': 'TestSubmit deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except TestSubmit.DoesNotExist:
            return Response({"error": "TestSubmit not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitByTestView(APIView):
    paginator = TestSubmitPagination()

    @extend_schema(
        summary="문제별 답변 조회",
        description="임시",
        tags=["Classroom-TestSubmit"],
        responses=TestSubmitSerializer,
    )
    def get(self, request, pk):
        try:
            queryset = TestSubmit.objects.filter(test=pk)
            if request.user.is_authenticated and request.user.is_teacher:
                result_page = self.paginator.paginate_queryset(queryset, request)
                serializer = TestSubmitSerializer(result_page, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestSubmitByTestUserView(APIView):
    @extend_schema(
        summary="임시",
        description="임시",
        tags=["Classroom-TestSubmit"],
        responses=TestSubmitSerializer,
    )
    def get(self, request, test_pk, user_pk):
        try:
            queryset = TestSubmit.objects.filter(test=test_pk, user=user_pk)
            if request.user.is_authenticated and (request.user.is_teacher or request.user == queryset.user):
                serializer = TestSubmitSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Not available to access"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# /TestSubmit 문제 답변
