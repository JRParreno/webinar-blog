from django.urls import path
from .views import (
    home, about,
    PostCreateView, PostDetailView,
    PostUpdateView, PostDeleteView,
    PostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('create/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name="about"),
]
