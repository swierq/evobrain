from django.conf.urls import patterns, url
from evobrain_web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)