from django.contrib import admin
from .models import Classroom, Test, LectureNote, Question, Comment, TestSubmit


admin.site.register(Classroom)
admin.site.register(Test)
admin.site.register(LectureNote)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(TestSubmit)
