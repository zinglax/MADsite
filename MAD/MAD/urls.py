from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'members.views.home', name='home'),
    url(r'^about', 'members.views.about', name='about'),
    url(r'^apps', 'members.views.apps', name='apps'),
    
 
    # New Member
    url(r'^new_member', 'members.views.new_member', name='new_member'),
    
    # Members
    url(r'^members', 'members.views.members', name='members'),
    
    # Export Database
    url(r'^export', 'members.views.export', name='export'),
    
)
