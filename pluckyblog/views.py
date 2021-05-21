from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ( 
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .forms import NewCommentForm

from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_posted')
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected

        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'),
                             author=self.request.user,
                             post_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instace.author = self.request.user
        return super().form_valid(form)
