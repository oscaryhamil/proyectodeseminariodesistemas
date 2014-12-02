from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categorias(models.Model):
	nombre=models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre
	class Meta():
		permissions=(
			("ver_categoria","permite ver las categorias"),
		)
class pregunta(models.Model):
	usuario=models.ForeignKey(User, null=True)
	categoria=models.ForeignKey(categorias)
	enunciado=models.TextField()
	respuesta1=models.CharField(max_length=200)
	respuesta2=models.CharField(max_length=200)
	respuesta3=models.CharField(max_length=200)
	respuesta4=models.CharField(max_length=200)
	respuesta_correcta=models.CharField(max_length=200)
	def __unicode__(self):
		return self.enunciado
	class Meta():
		permissions=(
			("mostrar_preguntas","permite ver las preguntas"),
			("ver_categoria_pregunta","permite ver las categorias de una pregunta"),
		)
class partida(models.Model):
	tipos=(('public','Publico'),('private','Privado'))
	cant_preguntas=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'))
	tiempo=(('10','10'),('15','15'),('20','20'),('25','25'),('30','30'),('35','35'),('40','40'),('45','45'),('50','50'),('55','55'),('60','60'))
	titulo=models.CharField(max_length=200)
	jugadores=models.PositiveIntegerField()
	tipo_partida=models.CharField(max_length=200,choices=tipos)
	preguntas=models.CharField(max_length=5, choices=cant_preguntas)
	tiempo_respuesta=models.CharField(max_length=5,choices=tiempo)
	categorias_sel=models.ManyToManyField(categorias, blank=False)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo