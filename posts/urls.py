
from posts.views import post_home,post_detail,post_create,post_update,post_delete

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [

    url(r'^$', post_home,name='posts'),
    url(r'^(?P<id>\d+)/$', post_detail,name='postdetail'),
    url(r'^create/$', post_create,name='postcreate'),
    url(r'^(?P<id>\d+)/edit/$', post_update,name='postupdate'),
    url(r'^(?P<id>\d+)/delete/$', post_delete,name='postdelete'),
]
