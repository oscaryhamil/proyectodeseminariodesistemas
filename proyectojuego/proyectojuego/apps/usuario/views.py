#encoding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def view_registro(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			usuario_nuevo=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=usuario_nuevo)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado")
	else:
			formulario_registro=fusuario()
	return render_to_response("usuario/user_registro.html",{"formulario":formulario_registro},RequestContext(request))
def view_login(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect("/user/perfil/")
				else:
					login(request,acceso)
					return HttpResponseRedirect("/user/active/")
			else:
				return HttpResponse("Error en los datos")
	else:
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{"formulario":formulario},RequestContext(request))
def view_logout(request):
	logout(request)
	return HttpResponseRedirect("/")

def view_perfil(request):
	return render_to_response("usuario/perfil.html",{},RequestContext(request))

def view_user_active(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/user/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/user/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("usuario/activar.html",{'formulario':formulario},RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
