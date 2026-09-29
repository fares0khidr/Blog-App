from django.urls import path

from .views import (
    MyPostsView,
    PostCreateView,
    PostDeleteView,
    PublishedPostDetailView,
    PublishedPostListView,
    PostUpdateView,
    SignUpView,
    UserLoginView,
    UserLogoutView,
)


urlpatterns = [
    path('', PublishedPostListView.as_view(), name='post-list'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('posts/<int:pk>/', PublishedPostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
