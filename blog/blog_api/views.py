from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    DjangoModelPermissionsOrAnonReadOnly

from .serializers import PostDetailsSerializers, CreatePost, CreateCommentSerializers
from post.models import Post, Comment


class PostDetailsView(RetrieveAPIView):
    queryset = (
        Post.objects.
            select_related("author").
            prefetch_related("comments")
    )
    serializer_class = PostDetailsSerializers


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all().select_related("author")
    serializer_class = CreatePost
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CreateCommentView(ListCreateAPIView):
    queryset = Comment.objects.all().select_related("author").prefetch_related("post")
    serializer_class = CreateCommentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)