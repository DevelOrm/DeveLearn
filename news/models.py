from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    written_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
