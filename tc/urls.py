# Copyright 2016 by Dane Collins
from django.conf.urls import patterns, url
from tc import views


urlpatterns = patterns('',
                       url(r'^select/$', views.select_test),
                       url(r'^overview/(?P<id>[\d]+)/$', views.overview),
                       url(r'^step/(?P<num>[\d.]+)[/]*$', views.display_step),
                       url(r'^set_test/(?P<test_id>[\d]+)/$', views.set_test),
                       )
