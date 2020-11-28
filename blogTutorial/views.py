from django.shortcuts import render
from .models import Post


def home(req):
    context = {
        'posts': Post.objects.all(),
    }
    return render(req, 'blogTutorial/home.html', context=context)


def about(req):
    return render(req, 'blogTutorial/about.html', {'title': 'sm About'})