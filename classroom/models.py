from django.db import models
from django.contrib.postgres.fields import ArrayField


class Classroom(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    class_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    tag = ArrayField(models.CharField(max_length=50, blank=True), null=True, blank=True)

    # def __str__(self):
    #     return f'{self.user} - {self.class_name}'


class Test(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.classroom} - {self.title} - {self.user}'


class LectureNote(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_file = models.FileField(upload_to='', null=True, blank=True)
    upload_image = models.ImageField(upload_to='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.classroom} - {self.title} - {self.user}'


class Question(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_image = models.ImageField(upload_to='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.classroom} - {self.title} - {self.user}'


class Comment(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)
    teaching_material = models.ForeignKey(LectureNote, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.test}{self.teaching_material}{self.question} - {self.content} - {self.user}'


class TestSubmit(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.test} - {self.user}'
