from django.db import models

# Create your models here.

class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respusta_opcional=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta