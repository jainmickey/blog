from django.conf.urls import patterns, include, url
from django.contrib import admin
from post.models import Post
from post.views import *

urlpatterns = patterns('',
        url(r'^$', PostListView.as_view(), name='post_list'),
        url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
        url(r'^tag/(?P<pk>\d+)/$', PostTagView.as_view(), name='tag_posts'),
        url(r'^category/(?P<pk>\d+)/$', PostCatView.as_view(), name='cat_posts'),

        #url(r'^admin/', include(admin.site.urls)),
)

