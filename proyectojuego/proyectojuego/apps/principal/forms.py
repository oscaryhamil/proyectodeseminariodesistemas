from django.forms import ModelForm
from django import forms
from .models import *

class ftema(ModelForm):
	class Meta:
		model=Tema

class fpregunta(ModelForm):
	class Meta:
		model=Pregunta