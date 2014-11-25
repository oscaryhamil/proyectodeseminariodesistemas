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

def registro_tema(request):
	titulo="Registro de Temas"
	temas=Tema.objects.all()
	if request.method=="POST":
		formulario=ftema(request.POST)
		if formulario.is_valid():
			formulario.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas}
			return render_to_response("principal/registro_temas.html",datos,context_instance=RequestContext(request))
	else:
		formualrio=ftema()
	datos={'titulo':titulo,'formualrio':formulario,'temas':temas}
	return render_to_response("principal/registro_temas.html",datos,context_instance=RequestContext(request))

