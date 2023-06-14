from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Pk: {self.pk} | Title: {self.title}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'author: {self.author} text: {self.text}'