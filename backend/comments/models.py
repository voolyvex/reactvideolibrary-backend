from django.db import models
from authentication.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=128)
    text = models.CharField(max_length=255)
    date_time = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)