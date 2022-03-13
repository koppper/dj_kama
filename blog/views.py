from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Tag, Post


def blog_get(request):
    obj = Post.objects.all()
    return render(request, 'blog/index.html', {'obj': obj})


def get_category(request):
    return render(request, 'blog/category.html')

