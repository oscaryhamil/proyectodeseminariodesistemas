from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#photo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,200),)

# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User,unique=True)
	pais=models.CharField(max_length="30",null=False)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((50,50),(200,200)))
	class Meta:
 		permissions=(("ver_perfil","permite ver el perfil"),("cambiar_perfil","permite modificar el perfil"),)




