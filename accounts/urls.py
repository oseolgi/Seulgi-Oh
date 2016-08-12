from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from . import views
# from blog import views
# from pokemongo import views as pokemongo_views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
