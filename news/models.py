from django.db import models


class News(models.Model):
    title = models.TextField(max_length=255)
    link = models.URLField(max_length=2048)
    written_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
