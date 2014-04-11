#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mfw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    #static(settings.STATIC_URL,'django.views.static.serve',{'document_root': settings.STATIC_URL}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')), #added
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('gmapi.urls.media')), # Use for debugging only.
    
    (r'^sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
    (r'^robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
)
