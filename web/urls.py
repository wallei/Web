from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.contrib.auth.views import login, logout
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'loginusuario.views.home', name='home'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'media_root':settings.MEDIA_ROOT,}
	),
    
)
