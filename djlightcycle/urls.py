from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tournament.views.index', name='index'),
    url(r'^scoreboard', 'tournament.views.scoreboard', name='scoreboard'),
    url(r'^upload', 'tournament.views.upload', name='upload'),
    url(r'^about', 'tournament.views.about', name='about'),
    url(r'^update_bot', 'tournament.views.update_bot', name='upload'),
    # url(r'^djlightcycle/', include('djlightcycle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)
