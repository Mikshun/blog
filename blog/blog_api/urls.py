from django.urls import path, include, re_path
from .views import PostListView, PostDetailsView, CreateCommentView

appname = 'blog_api'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailsView.as_view(), name='get_details'),
    path('comment/', CreateCommentView.as_view(), name='comment_list'),
    path('auth/', include('rest_framework.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]