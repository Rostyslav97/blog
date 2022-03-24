from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.SlugField(max_length=160, unique=True)
    status = models.BooleanField(null=False, blank=False, default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    amount_of_upvotes = models.IntegerField(null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

class Upvote(models.Model):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)