from django.shortcuts import render,render_to_response
from django.template import RequestContext
def principal(request):
	return render_to_response("base.html",{},RequestContext(request))

# Create your views here.
