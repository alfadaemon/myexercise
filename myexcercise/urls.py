from django.conf.urls import patterns, include, url

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myexcercise.views.home', name='home'),
    (r'^accounts/', include('userena.urls')),
    (r'^accounts/', include('accounts.urls')),
    #(r'^exercises/', include('exercises.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
