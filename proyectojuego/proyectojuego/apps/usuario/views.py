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
	return render_to_response("usuario/user_registro.html",{"formulario":formulario_registro},context_instance=RequestContext(request))
def view_login(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cont']>3:
			formulario2=fcaptcha(request.POST)
			if formulario2.is_valid():
				pass
			else:
				datos={'formulario':formulario,'formulario2':formulario2}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))		
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					del request.session['cont']
					return HttpResponseRedirect("/user/perfil/")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/user/active/")
			else:
				request.session['cont']=request.session['cont']+1
				var=request.session['cont']
				estado=True
				mensaje="Error en los datos "+str(var)
				if var>3:
					formulario2=fcaptcha()
					datos={'formulario':formulario,'formulario2':formulario2,'estado':estado,'mensaje':mensaje}
				else:
					datos={'formulario':formulario,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))		
	else:
		request.session['cont']=0
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))
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
			return render_to_response("usuario/activar.html",{"formulario":formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")

def modificar_perfil(request):
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=='POST':
			formulario=fperfil_modificar(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/usuario/"+str(usuario.id)+"/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response('modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")

