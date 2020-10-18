from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Post, Category

from main.forms import PostForm

class mainView(ListView):
    model = Post
    template_name = 'main/main.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'main/add_post.html'
    #fields = '__all__'
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'main/update_post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('main')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'main/add_category.html'
    fields = '__all__'
