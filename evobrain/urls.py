from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evobrain.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^evobrain/', include('evobrain_web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
