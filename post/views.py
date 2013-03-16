# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, CreateView
from post.models import Post, Tags, Category

class PostListView(ListView):
    context_object_name = 'post_list'
    template_name = 'post_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['all_tags'] = Tags.objects.all()
        context['all_categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['all_tags'] = Tags.objects.all()
        context['all_categories'] = Category.objects.all()
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_post_create.html'
    success_url = '/post/create/'

class PostTagView(ListView):
    context_object_name = 'posts'
    template_name = 'tag_posts.html'

    def get_context_data(self, **kwargs):
        context = super(PostTagView, self).get_context_data(**kwargs)
        id_received = self.kwargs['pk']
        context['tag_name'] = Tags.objects.get(id = id_received)
        return context

    def get_queryset(self):
        id_recieved = self.kwargs['pk']
        tag = Tags.objects.get(id = id_recieved)
        return tag.post_set.all()

class PostCatView(ListView):
    context_object_name = 'posts'
    template_name = 'cat_posts.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostCatView, self).get_context_data(**kwargs)
        id_received = self.kwargs['pk']
        context['cat_name'] = Category.objects.get(id = id_received)
        return context

    def get_queryset(self):
        id_recieved = self.kwargs['pk']
        cat = Category.objects.get(id = id_recieved)
        return Post.objects.filter(category = cat)
