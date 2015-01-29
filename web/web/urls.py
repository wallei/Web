from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$','commerce.views.lista_producto'),
    url(r'^$', 'commerce.views.login'),
    url(r'^login/$', 'commerce.views.login'),
    url(r'^perfil/$', 'commerce.views.perfil'),
    url(r'^salir/$', 'commerce.views.salir'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT}
	),
    
)
urlpatterns+= staticfiles_urlpatterns()