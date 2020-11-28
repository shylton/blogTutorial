from django.shortcuts import render


def home(req):
    return render(req, 'blogTutorial/home.html')


def about(req):
    return render(req, 'blogTutorial/about.html')