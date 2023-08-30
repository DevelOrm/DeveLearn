from django.contrib import admin
from .models import Classroom, Test, Board, TestComment, LectureNote, LectureNoteComment, Question, QuestionComment, \
    TestSubmit

admin.site.register(Classroom)
admin.site.register(Test)
admin.site.register(Board)
admin.site.register(TestComment)
admin.site.register(LectureNote)
admin.site.register(LectureNoteComment)
admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(TestSubmit)
