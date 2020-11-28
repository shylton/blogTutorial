from django.urls import path
from . import views

app_name = 'blogTutorial'
urlpatterns = [
    path('', views.home, name='blog_home'),  # host/blog
    path('about/', views.about, name='blog_about'),  # host/blog/about
]