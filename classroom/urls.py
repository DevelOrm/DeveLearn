from django.urls import path
from .views import ClassroomView, ClassroomDetailView, ClassroomTagView, TestBoardView, TestBoardDetailView, \
    TestBoardByClassView, TestView, TestDetailView, TestByBoardView, LectureNoteBoardView, LectureNoteBoardDetailView, \
    LectureNoteBoardByClassView, LectureNoteView, LectureNoteDetailView, LectureNoteByBoardView, QuestionBoardView, \
    QuestionBoardDetailView, QuestionBoardByClassView, QuestionView, QuestionDetailView, QuestionByBoardView, \
    CommentView, CommentDetailView, CommentByBoardView, TestSubmitView, TestSubmitDetailView, TestSubmitByTestView

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
    # path('<int:pk>/', ClassroomByTeacherView.as_view()),

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

    ## 질문 게시판
    # 질문 게시판 목록 조회 및 질문 게시판 생성
    path('question/', QuestionBoardView.as_view()),
    # 질문 게시판 상세 조회, 수정, 삭제
    path('question/detail/<int:pk>/', QuestionBoardDetailView.as_view()),
    # 클래스별 질문 게시판 조회
    path('question/<int:pk>/', QuestionBoardByClassView.as_view()),

    ## 질문 게시글
    # 질문 게시글 목록 조회 및 질문 게시글 생성
    path('question/', QuestionView.as_view()),
    # 질문 게시글 상세 조회, 수정, 삭제
    path('question/detail/<int:pk>/', QuestionDetailView.as_view()),
    # 게시판별 질문 게시판 조회
    path('question/<int:pk>/', QuestionByBoardView.as_view()),

    ## 댓글
    # 댓글 목록 조회 및 댓글 작성
    path('comment/', CommentView.as_view()),
    # 댓글 상세 조회, 삭제
    path('comment/detail/<int:pk>/', CommentDetailView.as_view()),
    # 게시글별 댓글 조회
    path('comment/<int:pk>/', CommentByBoardView.as_view()),

    ## 문제 답변
    # 제출한 문제 답변 조회 및 문제 답변 제출
    path('testsubmit/', TestSubmitView.as_view()),
    # 문제 답변 상세 조회
    path('testsubmit/detail/<int:pk>/', TestSubmitDetailView.as_view()),
    # 문제별 문제 답변 조회
    path('testsubmit/<int:pk>/', TestSubmitByTestView.as_view()),
]
