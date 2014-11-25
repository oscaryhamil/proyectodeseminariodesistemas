from django.db import models

# Create your models here.

class Tema(models.Model):
	nombre=models.CharField(max_length=50,unique=True)

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)

class Respuesta(models.Model):
	repuesta_correcta=models.CharField(max_length=500)
	repuesta_incorrecta=models.CharField(max_length=500)
	repuesta_opcional=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
