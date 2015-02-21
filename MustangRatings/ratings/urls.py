from django.conf.urls import patterns, url
from ratings import views

urlpatterns = patterns('',
   url(r'^$', views.main, name='main'),
   url(r'^list/(?P<class_id>[0-9]+)$', views.professor_list, name='list'),
   url(r'^detail/(?P<cpairing_id>[0-9]+)$', views.pairing_detail, name='detail'),
   url(r'^login/$', 'django.contrib.auth.views.login'),
)
