from django.conf.urls import patterns, url, include

from .api import UserList, UserDetail
from .api import PostList, PostDetail, UserPostList

user_url = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

post_urls = patterns('',
    url(r'^/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls))
)