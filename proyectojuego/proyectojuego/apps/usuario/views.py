from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def view_registro(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			usuario_nuevo=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=usuario_nuevo)
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado")
	else:
			formulario_registro=fusuario()
	return render_to_response("usuario/user_registro.html",{"formulario":formulario_registro},RequestContext(request))
