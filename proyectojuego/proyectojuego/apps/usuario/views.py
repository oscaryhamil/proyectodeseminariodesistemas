from django.shortcuts import render,render_to_response
from django.template import RequestContext
def index(request):
	return render_to_response("index.html",{},RequestContext(request))

# Create your views here.
