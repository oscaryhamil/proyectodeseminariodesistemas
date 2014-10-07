from django.conf.urls import patterns, include, url
from django.contrib import admin
#from apps.usuario.views import principal

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectojuego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^',(principal)),
    url(r'^', include('proyectojuego.apps.principal.urls')),
    url(r'^', include('proyectojuego.apps.usuario.urls')),
)
