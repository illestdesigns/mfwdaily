#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mfw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    #static(settings.STATIC_URL,'django.views.static.serve',{'document_root': settings.STATIC_URL}),
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('gmapi.urls.media')), # Use for debugging only.
    #(r'^$', 'myapp.views.index'),
)
