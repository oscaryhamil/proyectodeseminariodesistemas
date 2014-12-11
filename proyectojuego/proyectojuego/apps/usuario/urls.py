from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^user/registro/$',view_registro),
    url(r'^login/$',view_login),
    url(r'^logout/$',view_logout),
    url(r'^user/perfil/$',view_perfil),
    url(r'^user/active/$',view_user_active),
    url(r'^user/modificar/$',modificar_perfil),
    url(r'^conexionnode/$',conexionnode),
)
