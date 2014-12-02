from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.
def view_inicio(request):
	usuarios=User.objects.all()
	return render_to_response("principal/inicio.html",{'usuarios':usuarios},context_instance=RequestContext(request))
def crear_categoria(request):
	usuario=request.user #sirve para identificar el usuario
	#if (not usuario.has_perm("preguntas.add_categorias")):
		#return HttpResponseRedirect("/preguntas/catrestringida/")
	if request.method=="POST":
		fcategoria=categoriaForm(request.POST)
		if fcategoria.is_valid():
			fcategoria.save()
			return HttpResponseRedirect("/user/perfil/")
	fcategoria=categoriaForm()
	return render_to_response("principal/crear_categorias.html",{"fcategoria":fcategoria},RequestContext(request))
def crear_pregunta(request):
	usuario=request.user
	#if(not usuario.has_perm("preguntas.add_mpregunta")):
		#return HttpResponseRedirect("/preguntas/pregrestringida/")
	if request.method=="POST":
		fpregunta=preguntaForm(request.POST)
		if fpregunta.is_valid():
			fpregunta.save()
			return HttpResponseRedirect("/user/perfil/")
	fpregunta=preguntaForm()
	return render_to_response("principal/crear_pregunta.html",{"fpregunta":fpregunta},RequestContext(request))

def ver_preguntas(request):
	lista=mpregunta.objects.all()
	return render_to_response("principal/verpreguntas.html",{"lista":lista},RequestContext(request))
def categoria_restringida(request):
	return render_to_response("principal/catrestringida.html",{},RequestContext(request))
def pregunta_restringida(request):
	return render_to_response("principal/pregrestringida.html",{},RequestContext(request))
def ver_categoria(request):
	lista=categorias.objects.all()
	return render_to_response("principal/vercategorias.html",{"lista":lista},RequestContext(request))
def control_preguntas(request):
	lista=mpregunta.objects.all()
	return render_to_response("principal/control_preguntas.html",{"lista":lista},RequestContext(request))
def modificar_pregunta(request,id):
	pregunta=get_object_or_404(mpregunta,pk=id)
	if request.method=="POST":
		fpregunta=preguntaForm(request.POST,instance=pregunta)
		if fpregunta.is_valid():
			fpregunta.save()
			return HttpResponse("Pregunta modificada exitosamente")
	else:
		fpregunta=preguntaForm(instance=pregunta)
	return render_to_response("principal/modificar.html",{"fpregunta":fpregunta},RequestContext(request))
def detalle_pregunta(request):
	lista=mpregunta.objects.all()
	return render_to_response("principal/detalles_pregunta.html",{"lista":lista},RequestContext(request))
def ver_detalles(request,id):
	pregunta=get_object_or_404(mpregunta,pk=id)
	return render_to_response("principal/verdetalles.html",{"pregunta":pregunta},RequestContext(request))
def eliminar_pregunta(request,id):
	aux=mpregunta.objects.get(pk=id)
	borrar=aux.delete()
	return HttpResponseRedirect("/principal/preguntaseliminar/")
def lista_preguntas_eliminar(request):
	lista=mpregunta.objects.all()
	return render_to_response("principal/eliminar.html",{"lista":lista},RequestContext(request))
def crear_partida(request):
	if (request.method=="POST"):
		usuario=User.objects.get(username=request.user)
		form=partidaForm(request.POST)
		#usuario=User.objects.get(username=request.user)
		if(form.is_valid()):
			obj=form.save(commit=False)
			obj.usuario=usuario
			obj.save()
			form.save_m2m()
			return HttpResponseRedirect("/trivia/")
	else:
		form=partidaForm()
	return render_to_response("principal/crearpartida.html",{"form":form},RequestContext(request))
def lista_partidas(request):
	lista=partida.objects.filter(tipo_partida='public')
	return render_to_response("principal/listapartidas.html",{"lista":lista},RequestContext(request))