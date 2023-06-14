from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "title", "author", "description"


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = "author", "text", "post"
