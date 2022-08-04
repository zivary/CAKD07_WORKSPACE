# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post


# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'post' : posts,
#         }
#     )s