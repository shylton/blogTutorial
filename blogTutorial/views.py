from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse('<h1>Blog home by sm</h1>')
