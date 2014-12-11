#encoding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group,Permission
from django.contrib.sessions.models import Session
from django.contrib.auth import login, authenticate,logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required


# Create your views here.
def view_registro(request):
	menu=permisos(request)
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			usuario_nuevo=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=usuario_nuevo)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return  HttpResponseRedirect("/login/")
	else:
			formulario_registro=fusuario()
	return render_to_response("usuario/user_registro.html",{"formulario":formulario_registro},context_instance=RequestContext(request))
def view_login(request):
	menu=permisos(request)
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
					p=SessionStore()
					p["name"]=usuario
					p["estado"]="conectado"
					p.save()
					request.session["idkey"]=p.session_key
					request.session["name"]=usuario
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
@login_required(login_url ='/login/')
def view_logout(request):
	menu=permisos(request)
	# p=SessionStore(session_key=request.session["idkey"])
	# p["estado"]="desconectado"
	# p["name"]=""
	# p.save()
	logout(request)
	return HttpResponseRedirect("/")
@login_required(login_url ='/login/')
def view_perfil(request):
	menu=permisos(request)
	usuario=User.objects.get(username=request.user)
	# try:
	# 	perfil=Perfil.objects.get(user=usuario)
 #    		return HttpResponseRedirect("/user/perfil/")
	# except Perfil.DoesNotExist:
 #    		usuario_nuevo=User.objects.get(username=usuario)
 #    		perfil=Perfil.objects.create(user=usuario_nuevo)
 #    #creas y le envias a su perfil
	return render_to_response("usuario/perfil.html",{},RequestContext(request))

def view_user_active(request):
	menu=permisos(request)
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
				return HttpResponseRedirect("/user/perfil/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response('modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
def conexionnode(request):
	idsession=request.session["idkey"]
	return HttpResponseRedirect("http://localhost:3000/django/"+idsession)

#def chat(request):
	#idsession=request.session["idkey"]
	#return HttpResponseRedirect("http://localhost:3000/django/"+idsession)


def permisos(request):
	listadepermisos=[]
	usuario=request.user
	if usuario.has_perm("preguntas.add_categorias"):
		listadepermisos.append({"url":"/preguntas/crearcategorias/","label":"agregar categorias"})
	if usuario.has_perm("preguntas.add_mpregunta"):
		listadepermisos.append({"url":"/preguntas/crearpreguntas/","label":"agregar preguntas"})
	if usuario.has_perm("preguntas.mostrar_preguntas"):
		listadepermisos.append({"url":"/preguntas/verpreguntas/","label":"ver preguntas"})
	if usuario.has_perm("preguntas.ver_categoria"):
		listadepermisos.append({"url":"/preguntas/vercategorias/","label":"ver categorias"})
	return listadepermisos