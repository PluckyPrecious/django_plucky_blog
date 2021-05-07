from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


import pytz
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField (max_length=100)

    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post_connected = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail')