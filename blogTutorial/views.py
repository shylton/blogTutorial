from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# def home(req):
#     context = {
#         'posts': Post.objects.all(),
#     }
#     return render(req, 'blogTutorial/home.html', context=context)


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    # changing defaults because template already created in this case
    template_name = 'blogTutorial/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  # feeds the form

    def form_valid(self, form):
        """override parent func to set the author before saving"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # runs parent func


def about(req):
    return render(req, 'blogTutorial/about.html', {'title': 'sm About'})