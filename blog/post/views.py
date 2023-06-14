from django.shortcuts import render
from .models import Post

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView


class PostsListView(ListView):
    model = Post
    queryset = Post.objects.all()
    paginate_by = 10
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    queryset = (
        Post.objects.
        select_related("author").
        prefetch_related("comments")
    )

class RegisterUser(TemplateView):
    template_name = "post/register.html"