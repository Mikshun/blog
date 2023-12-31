from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Post, Comment
from rest_framework.relations import StringRelatedField

class CommentSerializers(serializers.ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Comment
        fields = 'author', 'text'

class PostDetailsSerializers(serializers.ModelSerializer):
    author = StringRelatedField()
    comments = CommentSerializers(many=True)

    class Meta:
        model = Post
        fields = 'title', 'author', 'description', 'comments'

class CreatePost(serializers.ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Post
        fields = 'pk', 'title', 'author', 'description'

class CreateCommentSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = 'author', 'text', 'post'