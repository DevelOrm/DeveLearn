from django.db import models
from django.contrib.postgres.fields import ArrayField


class Classroom(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    class_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = ArrayField(models.CharField(max_length=50, blank=True), null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'self.user - {self.class_name}'


class TestBoard(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.classroom} - {self.title} - self.user'


class Test(models.Model):
    board = models.ForeignKey(TestBoard, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    solution = ArrayField(models.CharField(max_length=50, blank=True), null=True, blank=True)
    auto_score = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.board} - {self.title} - self.user'


class LectureNoteBoard(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.classroom} - {self.title} - self.user'


class LectureNote(models.Model):
    board = models.ForeignKey(LectureNoteBoard, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_file = models.FileField(upload_to='lecturenote/file/', null=True, blank=True)
    upload_image = models.ImageField(upload_to='lecturenote/image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.board} - {self.title} - self.user'


class QuestionBoard(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.classroom} - {self.title} - self.user'


class Question(models.Model):
    board = models.ForeignKey(QuestionBoard, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_image = models.ImageField(upload_to='question/image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.board} - {self.title} - self.user'


class TestComment(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.test} - {self.content} - self.user'


class LectureNoteComment(models.Model):
    lecture_note = models.ForeignKey(LectureNote, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.lecture_note} - {self.content} - self.user'


class QuestionComment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.question} - {self.content} - self.user'


class TestSubmit(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_answer = models.TextField()
    answer_status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.test} - self.user'
