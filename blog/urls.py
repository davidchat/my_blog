from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    path('post/new/', views.create_post, name='post-create'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.update_post, name='post-update'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('comment/<int:pk>/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    path('about/', views.about, name='blog-about'),
]