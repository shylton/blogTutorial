from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    # changing defaults because template already created in this case
    template_name = 'blogTutorial/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogTutorial:blog_home')

    def test_func(self):
        """UserPassesTestMixin func to check that currently logged in
        user only updates his own posts"""
        post = self.get_object()

        return self.request.user == post.author


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # feeds the form

    def form_valid(self, form):
        """override parent func to set the author before saving"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # runs parent func


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # feeds the form

    def form_valid(self, form):
        """override parent func to set the author before saving"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # runs parent func

    def test_func(self):
        """UserPassesTestMixin func to check that currently logged in
        user only updates his own posts"""
        post = self.get_object()

        return self.request.user == post.author


def about(req):
    return render(req, 'blogTutorial/about.html', {'title': 'sm About'})