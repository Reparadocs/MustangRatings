from django.conf.urls import patterns, url
from ratings import views

urlpatterns = patterns('',
   url(r'^$', views.main, name='main'),
   url(r'^list/$', views.professor_list, name='list'),
   url(r'^detail/$', views.professor_detail, name='detail'),
)
