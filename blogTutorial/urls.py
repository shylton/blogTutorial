from django.urls import path
# from .views import PostListView, PostDetailView
from . import views

app_name = 'blogTutorial'
urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),  # host/blog
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog_about'),  # host/blog/about
]