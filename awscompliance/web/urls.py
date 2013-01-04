'''
Created on 04-Jan-2013

@author: shubham
'''

from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    
    url('results$', views.return_port_details, name='port_details'),
        
    #url(r'^(?P<project_id>\d+)/results/$', views.results, name='results'),
        
    #url(r'^(?P<project_id>\d+)/vote/$', views.vote, name='vote'),

    )