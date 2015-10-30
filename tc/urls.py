from django.conf.urls import patterns, url
from tc import views


urlpatterns = patterns('',
                       url(r'^new/(?P<test_name>[\w]+)/$', views.new_test),
                       url(r'^type/(?P<id>[\d]+)/$', views.select_type),
                       url(r'^overview/(?P<id>[\d]+)/$', views.overview),
                       )
