from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


import pytz
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL, null=True,
        related_name='posts',
    )
    date_updated = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_posted']
    
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

    class Meta:
        ordering = ['date_posted']

    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

    def get_absolute_url(self):
        return reverse('post_detail')