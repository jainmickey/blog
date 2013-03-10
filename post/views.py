# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, CreateView
from post.models import Post, Tags

class PostListView(ListView):
    context_object_name = 'post_list'
    template_name = 'post_list.html'
    model = Post

class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'
    model = Post

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_post_create.html'
    success_url = '/post/create/'

class PostTagView(ListView):
    context_object_name = 'tag_posts'
    template_name = 'tag_posts.html'
    model = Tags
