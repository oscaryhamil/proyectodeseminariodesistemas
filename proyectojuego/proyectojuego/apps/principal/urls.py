from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^$',inicio_view, name='Inicio'),
    url(r'^registro/tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    #url(r'^registro/pregunta/$',registro_pregunta, name='Pregunta'),
    #url(r'^permit/$',error_permisos),
    url(r'^permisos/$',error_permisos),
)