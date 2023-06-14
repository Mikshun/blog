from django.urls import path
from .views import PostsListView, PostDetailView, RegisterUser

appname = 'post'
urlpatterns = [
    path('', PostsListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('register', RegisterUser.as_view(), name='register')
]