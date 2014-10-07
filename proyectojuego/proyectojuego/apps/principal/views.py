from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def view_inicio(request):
	return render_to_response("principal/inicio.html",{},RequestContext(request))
