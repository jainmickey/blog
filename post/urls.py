from django.conf.urls import patterns, include, url
from post.models import Post
from post.views import *

urlpatterns = patterns('',
        url(r'^$', PostListView.as_view(), name='post_list'),
        url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
        url(r'^(?P<pk>\w+)/$', PostTagView.as_view(), name='tag_posts'),
)

