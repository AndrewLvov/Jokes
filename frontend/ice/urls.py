from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jokes/', 'ice.views.jokes', name='jokes'),

    # url(r'^admin/', include(admin.site.urls)),
)
