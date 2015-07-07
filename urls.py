from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact/', include('contact.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('home.urls')),
)
