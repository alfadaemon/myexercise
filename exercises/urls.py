from django.conf.urls import patterns, include, url

from exercises import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'workout/$', views.workout, name='workout'),
)