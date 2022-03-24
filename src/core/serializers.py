from rest_framework import serializers
from core.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("id", )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("author_name", "content", "creation_date")