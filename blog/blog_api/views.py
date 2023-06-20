from django.http import HttpRequest, HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

from .serializers import PostDetailsSerializers, CreatePost, CreateCommentSerializers
from post.models import Post, Comment
from rest_framework.response import Response

class PostDetailsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        response.headers['Staff'] = request.user.is_staff
        response.headers['Auth'] = request.user.is_authenticated
        return response
    queryset = (
        Post.objects.
            select_related("author").
            prefetch_related("comments")
    )
    serializer_class = PostDetailsSerializers


class PostListView(ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers['Staff'] = request.user.is_staff
        response.headers['Auth'] = request.user.is_authenticated
        return response

    queryset = Post.objects.all().select_related("author")
    serializer_class = CreatePost
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CreateCommentView(ListCreateAPIView):
    def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            response = Response(serializer.data)
            response.headers['Staff'] = request.user.is_staff
            response.headers['Auth'] = request.user.is_authenticated
            return response

    serializer_class = CreateCommentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
                queryset = Comment.objects.all().select_related("author").prefetch_related("post")
                item_post = self.request.query_params.get('post')
                if item_post:
                    queryset = queryset.filter(post=item_post)
                return queryset


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)