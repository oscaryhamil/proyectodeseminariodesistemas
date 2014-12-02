from django.forms import ModelForm
from django import forms
from .models import *
#from django.forms.extras.widgets import *
tipos=(('public','Publico'),('private','Privado'))
cant_preguntas=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'))
tiempo=(('10 segundos','10 segundos'),('15 segundos','15 segundos'),('20 segundos','20 segundos'),('25 segundos','25 segundos'),('30 segundos','30 segundos'),('35 segundos','35 segundos'),('40 segundos','40 segundos'),('45 segundos','45 segundos'),('50 segundos','50 segundos'),('55 segundos','55 segundos'),('60 segundos','60 segundos'))
categoria=categorias.objects.all()
class categoriaForm(forms.ModelForm):
	class Meta:
		model=categorias
		exclude=["usuario"]
class preguntaForm(ModelForm):
	class Meta:
		model=pregunta
		exclude=["usuario"]
class partidaForm(ModelForm):
	tipo_partida=forms.ChoiceField(widget=forms.RadioSelect,choices=tipos)
	categorias_sel=forms.ModelMultipleChoiceField(queryset=categorias.objects.all(),widget=forms.CheckboxSelectMultiple()) 
	class Meta:
		model=partida
		exclude=["usuario"]