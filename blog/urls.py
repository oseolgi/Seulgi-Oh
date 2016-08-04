from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/edit/$', views.comment_edit, name='comment_edit'),
]