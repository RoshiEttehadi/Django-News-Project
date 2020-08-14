from django.contrib.auth import get_user_model
from django.db import models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories"
    )
    url = models.URLField(max_length=200)

