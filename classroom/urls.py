from django.urls import path
from .views import ClassroomView, ClassroomDetailView, ClassroomTagView, BoardView, BoardDetailView, \
    BoardByClassView, TestView, TestDetailView, TestByBoardView, TestCommentView, TestCommentDetailView, \
    TestCommentByPostView, LectureNoteView, LectureNoteDetailView, LectureNoteByBoardView, \
    LectureNoteCommentView, LectureNoteCommentDetailView, LectureNoteCommentByPostView, QuestionView, \
    QuestionDetailView, QuestionByBoardView, TestSubmitView, TestSubmitDetailView, TestSubmitByTestView, \
    QuestionCommentView, QuestionCommentDetailView, QuestionCommentByPostView, ClassroomByTeacherView, \
    TestSubmitByTestUserView, SubscriptionView, SubscriptionDetailView, SubscriptionByUserView, \
    TestSubmitCurrentUserView

app_name = 'classroom'

urlpatterns = [
    path('', ClassroomView.as_view()),
    path('detail/<int:pk>/', ClassroomDetailView.as_view()),
    path('tag/', ClassroomTagView.as_view()),
    path('<int:pk>/', ClassroomByTeacherView.as_view()),

    path('<int:pk>/subscription/', SubscriptionView.as_view()),
    path('subscription/detail/<int:pk>/', SubscriptionDetailView.as_view()),
    path('user-subscription/<int:pk>/', SubscriptionByUserView.as_view()),

    path('board/', BoardView.as_view()),
    path('board/detail/<int:pk>/', BoardDetailView.as_view()),
    path('board/<int:pk>/', BoardByClassView.as_view()),

    path('test/post/', TestView.as_view()),
    path('test/post/detail/<int:pk>/', TestDetailView.as_view()),
    path('test/post/<int:pk>/', TestByBoardView.as_view()),

    path('test/comment/', TestCommentView.as_view()),
    path('test/comment/detail/<int:pk>/', TestCommentDetailView.as_view()),
    path('test/comment/<int:pk>/', TestCommentByPostView.as_view()),

    path('lecture_note/post/', LectureNoteView.as_view()),
    path('lecture_note/post/detail/<int:pk>/', LectureNoteDetailView.as_view()),
    path('lecture_note/post/<int:pk>/', LectureNoteByBoardView.as_view()),

    path('lecture_note/comment/', LectureNoteCommentView.as_view()),
    path('lecture_note/comment/detail/<int:pk>/', LectureNoteCommentDetailView.as_view()),
    path('lecture_note/comment/<int:pk>/', LectureNoteCommentByPostView.as_view()),

    path('question/post/', QuestionView.as_view()),
    path('question/post/detail/<int:pk>/', QuestionDetailView.as_view()),
    path('question/post/<int:pk>/', QuestionByBoardView.as_view()),

    path('question/comment/', QuestionCommentView.as_view()),
    path('question/comment/detail/<int:pk>/', QuestionCommentDetailView.as_view()),
    path('question/comment/<int:pk>/', QuestionCommentByPostView.as_view()),

    path('testsubmit/', TestSubmitView.as_view()),
    path('testsubmit/detail/<int:pk>/', TestSubmitDetailView.as_view()),
    path('testsubmit/<int:pk>/', TestSubmitByTestView.as_view()),
    path('testsubmit/<int:test_pk>/user/<int:user_pk>/', TestSubmitByTestUserView.as_view()),
    path('testsubmit/current-user/', TestSubmitCurrentUserView.as_view()),
]
