from django.shortcuts import render


posts = [
    {
        'author': 'Tommy',
        'title': 'Post 1',
        'content': 'hola soy Tommy guac<br>me gusta muy guac.',
        'date_posted': '27 aug 2020',
    },
    {
        'author': 'Johnny Cerrantes',
        'title': 'Post 2',
        'content': 'hola soy J Bones!',
        'date_posted': '28 aug 2020',
    },
]


def home(req):
    context = {
        'posts': posts,
    }
    return render(req, 'blogTutorial/home.html', context=context)


def about(req):
    return render(req, 'blogTutorial/about.html', {'title': 'sm About'})