from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'members.views.home', name='home'),
    url(r'^about', 'members.views.about', name='about'),
    url(r'^apps', 'members.views.apps', name='apps'),
    
                       
)
