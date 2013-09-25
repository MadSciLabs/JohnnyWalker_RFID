from django.conf.urls.defaults import patterns, include, url
from jwrfid import views

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    url(r'^(?P<_rfid>\d+)/(?P<_type>[a-z]+)$', views.swipe, name='swipe'),
    url(r'^(?P<_type>[a-z]+)/$', views.station, name='station'),
    url(r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls))
)
