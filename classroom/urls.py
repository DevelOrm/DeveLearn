from django.urls import path
from .views import ClassroomView, ClassroomDetailView, ClassroomTagView, TestBoardView, TestBoardDetailView, \
    TestBoardByClassView, TestView, TestDetailView, TestByBoardView, TestCommentView, TestCommentDetailView, \
    TestCommentByPostView, LectureNoteBoardView, LectureNoteBoardDetailView, \
    LectureNoteBoardByClassView, LectureNoteView, LectureNoteDetailView, LectureNoteByBoardView, \
    LectureNoteCommentView, LectureNoteCommentDetailView, LectureNoteCommentByPostView, QuestionBoardView, \
    QuestionBoardDetailView, QuestionBoardByClassView, QuestionView, QuestionDetailView, QuestionByBoardView, \
    TestSubmitView, TestSubmitDetailView, TestSubmitByTestView, QuestionCommentView, QuestionCommentDetailView, \
    QuestionCommentByPostView, AllBoardByClassView, ClassroomByTeacherView, TestSubmitByTestUserView, SubscriptionView,\
    SubscriptionDetailView, SubscriptionByUserView

app_name = 'classroom'

urlpatterns = [
    ## 클래스
    # 클래스 목록 조회 및 클래스 생성
    path('', ClassroomView.as_view()),
    # 클래스 상세 조회, 수정, 삭제
    path('detail/<int:pk>/', ClassroomDetailView.as_view()),
    # 클래스 태그 조회
    path('tag/', ClassroomTagView.as_view()),
    # 교사별 클래스 조회
    path('<int:pk>/', ClassroomByTeacherView.as_view()),
    # 특정 클래스의 모든 게시판 조회
    path('board/', AllBoardByClassView.as_view()),

    ## 구독 정보
    # 구독 정보 조회 및 구독 정보 생성
    path('<int:pk>/subscription/', SubscriptionView.as_view()),
    # 구독 정보 상세 조회, 수정, 삭제
    path('subscription/detail/<int:pk>/', SubscriptionDetailView.as_view()),
    # 사용자별 구독 정보 조회
    path('user-subscription/<int:pk>/', SubscriptionByUserView.as_view()),

    ## 문제 게시판
    # 문제 게시판 목록 조회 및 문제 게시판 생성
    path('test/', TestBoardView.as_view()),
    # 문제 게시판 상세 조회, 수정, 삭제
    path('test/detail/<int:pk>/', TestBoardDetailView.as_view()),
    # 클래스별 문제 게시판 조회
    path('test/<int:pk>/', TestBoardByClassView.as_view()),

    ## 문제 게시글
    # 문제 게시글 목록 조회 및 문제 게시판 생성
    path('test/post/', TestView.as_view()),
    # 문제 게시글 상세 조회, 수정, 삭제
    path('test/post/detail/<int:pk>/', TestDetailView.as_view()),
    # 게시판별 문제 게시글 조회
    path('test/post/<int:pk>/', TestByBoardView.as_view()),

    ## 문제 게시글 댓글
    # 문제 게시글 댓글 목록 조회 및 댓글 작성
    path('test/comment/', TestCommentView.as_view()),
    # 문제 게시글 댓글 상세 조회, 삭제
    path('test/comment/detail/<int:pk>/', TestCommentDetailView.as_view()),
    # 게시글별 댓글 조회
    path('test/comment/<int:pk>/', TestCommentByPostView.as_view()),

    ## 강의자료 게시판
    # 강의자료 게시판 목록 조회 및 강의자료 게시판 생성
    path('lecturenote/', LectureNoteBoardView.as_view()),
    # 강의자료 게시판 상세 조회, 수정, 삭제
    path('lecturenote/detail/<int:pk>/', LectureNoteBoardDetailView.as_view()),
    # 클래스별 강의자료 게시판 조회
    path('lecturenote/<int:pk>/', LectureNoteBoardByClassView.as_view()),

    ## 강의자료 게시글
    # 강의자료 게시글 목록 조회 및 강의자료 게시글 생성
    path('lecturenote/post/', LectureNoteView.as_view()),
    # 강의자료 게시글 상세 조회, 수정, 삭제
    path('lecturenote/post/detail/<int:pk>/', LectureNoteDetailView.as_view()),
    # 게시판별 강의자료 게시글 조회
    path('lecturenote/post/<int:pk>/', LectureNoteByBoardView.as_view()),

    ## 강의자료 게시글 댓글
    # 강의자료 게시글 댓글 목록 조회 및 댓글 작성
    path('lecturenote/comment/', LectureNoteCommentView.as_view()),
    # 강의자료 게시글 댓글 상세 조회, 삭제
    path('lecturenote/comment/detail/<int:pk>/', LectureNoteCommentDetailView.as_view()),
    # 게시글별 댓글 조회
    path('lecturenote/comment/<int:pk>/', LectureNoteCommentByPostView.as_view()),

    ## 질문 게시판
    # 질문 게시판 목록 조회 및 질문 게시판 생성
    path('question/', QuestionBoardView.as_view()),
    # 질문 게시판 상세 조회, 수정, 삭제
    path('question/detail/<int:pk>/', QuestionBoardDetailView.as_view()),
    # 클래스별 질문 게시판 조회
    path('question/<int:pk>/', QuestionBoardByClassView.as_view()),

    ## 질문 게시글
    # 질문 게시글 목록 조회 및 질문 게시글 생성
    path('question/post/', QuestionView.as_view()),
    # 질문 게시글 상세 조회, 수정, 삭제
    path('question/post/detail/<int:pk>/', QuestionDetailView.as_view()),
    # 게시판별 질문 게시판 조회
    path('question/post/<int:pk>/', QuestionByBoardView.as_view()),

    ## 질문 게시글 댓글
    # 질문 게시글 댓글 목록 조회 및 댓글 작성
    path('question/comment/', QuestionCommentView.as_view()),
    # 질문 게시글 댓글 상세 조회, 삭제
    path('question/comment/detail/<int:pk>/', QuestionCommentDetailView.as_view()),
    # 게시글별 댓글 조회
    path('question/comment/<int:pk>/', QuestionCommentByPostView.as_view()),

    ## 문제 답변
    # 제출한 문제 답변 조회 및 문제 답변 제출
    path('testsubmit/', TestSubmitView.as_view()),
    # 문제 답변 상세 조회
    path('testsubmit/detail/<int:pk>/', TestSubmitDetailView.as_view()),
    # 문제별 문제 답변 조회
    path('testsubmit/<int:pk>/', TestSubmitByTestView.as_view()),
    # 문제+사용자별 답변 조회
    path('testsubmit/<int:test_pk>/user/<int:user_pk>/', TestSubmitByTestUserView.as_view()),
]
