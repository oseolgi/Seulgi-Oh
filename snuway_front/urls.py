from django.conf.urls import url
from . import views

app_name = 'snuway_front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^my$', views.my, name='my'),
    url(r'^lend$', views.lend, name='lend'),
    url(r'^lend_list$', views.lend_list, name='lend_list'),
]