from django.urls import path
from .views import ClassroomView

app_name = 'classroom'

urlpatterns = [
    ## 클래스
    # 클래스 목록 조회 및 클래스 생성
    path('', ClassroomView.as_view()),
    # 클래스 삭제
    path('delete/<int:pk>/', ClassroomView.as_view()),
    # 클래스 수정
    path('update/<int:pk>/', ClassroomView.as_view()),
    # 클래스 상세 조회
    # path('detail/<int:pk>/', ClassroomDetailView.as_view()),
    # 클래스 태그 조회
    # path('tag/<str:slug>/', ClassroomTagView.as_view()),
    # 교사별 클래스 조회
    # path('<str:user>/', ClassroomTeacherView.as_view()),

    ## 문제 게시판
    # 문제 게시판 목록 조회 및 문제 게시판 생성
    # path('test/', TestBoardView.as_view()),
    # 문제 게시판 삭제
    # path('test/<int:pk>/', TestBoardView.as_view()),
    # 문제 게시판 수정
    # path('test/update/<int:pk>/', TestBoardView.as_view()),
    # 문제 게시판 상세 조회
    # path('test/detail/<int:pk>/', TestBoardDetailView.as_view()),
    # 클래스별 문제 게시판 조회
    # path('test/<str:classroom>/', TestBoardClassView.as_view()),

    ## 강의자료 게시판
    # 강의자료 게시판 목록 조회 및 강의자료 게시판 생성
    # path('lecturenote/', LectureNoteView.as_view()),
    # 강의자료 게시판 삭제
    # path('lecturenote/<int:pk>/', LectureNoteView.as_view()),
    # 강의자료 게시판 수정
    # path('lecturenote/update/<int:pk>/', LectureNoteView.as_view()),
    # 강의자료 게시판 상세 조회
    # path('lecturenote/detail/<int:pk>/', LectureNoteDetailView.as_view()),
    # 클래스별 강의자료 게시판 조회
    # path('lecturenote/<str:classroom>/', LectureNoteClassView.as_view()),

    ## 질문 게시판
    # 질문 게시판 목록 조회 및 질문 게시판 생성
    # path('question/', QuestionView.as_view()),
    # 질문 게시판 삭제
    # path('question/<int:pk>/', QuestionView.as_view()),
    # 질문 게시판 수정
    # path('question/update/<int:pk>/', QuestionView.as_view()),
    # 질문 게시판 상세 조회
    # path('question/detail/<int:pk>/', QuestionDetailView.as_view()),
    # 클래스별 질문 게시판 조회
    # path('question/<str:classroom>/', QuestionClassView.as_view()),

    ## 댓글
    # 댓글 목록 조회 및 댓글 작성
    # path('comment/', CommentView.as_view()),
    # 댓글 삭제
    # path('comment/<int:pk>/', CommentView.as_view()),
    # 댓글 수정
    # path('comment/update/<int:pk>/', CommentView.as_view()),
    # 댓글 상세 조회
    # path('comment/detail/<int:pk>/', CommentDetailView.as_view()),
    # 게시판별 댓글 조회
    # path('comment/<str:board>/', CommentBoardView.as_view()),

    ## 문제 답변
    # 제출한 문제 답변 조회 및 문제 답변 제출
    # path('testsubmit/', TestSubmitView.as_view()),
    # 문제 답변 상세 조회
    # path('testsubmit/detail/<int:pk>/', TestSubmitDetailView.as_view()),
    # 문제별 문제 답변 조회
    # path('testsubmit/<str:test>/', TestSubmitTestView.as_view()),
]
