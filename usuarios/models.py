from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre_usuario=models.CharField(max_length=200)
    apellido_usuario=models.CharField(max_length=200)
    edad_usuario=models.PositiveIntegerField(default=0)
