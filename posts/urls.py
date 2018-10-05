from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	subject_detail,
	blog_subject_all,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^subject/$', blog_subject_all, name='blog_subject_all'),
	url(r'^subject/(?P<url>.+)/$', subject_detail, name='subject_detail'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
