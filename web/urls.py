from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','commerce.views.lista_producto'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT}
	),
    
)
