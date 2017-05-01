from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'mysite.views.about', name='about'),
    url(r'^currency/', 'mysite.views.crncy', name='crncy'),
    url(r'^result/', 'mysite.views.result', name='result'),
]
