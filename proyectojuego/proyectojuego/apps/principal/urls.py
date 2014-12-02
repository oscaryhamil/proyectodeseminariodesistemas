from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$',view_inicio,name='Inicio'),
    url(r'^principal/crearcategorias/$',crear_categoria),
    url(r'^principal/crearpreguntas/$',crear_pregunta),
    url(r'^verpreguntas/$',ver_preguntas),
    url(r'^/principal/vercategorias/$',ver_categoria),
    url(r'^catrestringida/$',categoria_restringida),
    url(r'^pregrestringida/$',pregunta_restringida),
    url(r'^controlpreguntas/$',control_preguntas),
    url(r'^detallespreguntas/$',detalle_pregunta),
    url(r'^modificar/(?P<id>\d+)/$',modificar_pregunta,name='modificar_pregunta'),
    url(r'^verdetallepregunta/(?P<id>\d+)/$',ver_detalles,name='ver_detalles'),
    url(r'^eliminarpregunta/(?P<id>\d+)/$',eliminar_pregunta,name='eliminar_pregunta'),
    url(r'^preguntaseliminar/$',lista_preguntas_eliminar),
    url(r'^crearpartida/$',crear_partida),
    url(r'^listapartidas/$',lista_partidas),
)