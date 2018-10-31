from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    perfil= models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Rol(models.Model):
    descripcion=models.CharField(max_length=30)

class Servicio(models.Model):
    descripcion=models.CharField(max_length=30)

class Localidad(models.Model):
    num_localidad=models.IntegerField()
    descripcion=models.CharField(max_length=30)

class Barrio(models.Model):
    descripcion=models.CharField(max_length=30)

class Poblacion(models.Model):
    descripcion=models.CharField(max_length=30)

class Residencia(models.Model):
    descripcion=models.CharField(max_length=30)

class Zona(models.Model):
    descripcion=models.CharField(max_length=30)

class Estado(models.Model):
    descripcion=models.CharField(max_length=30)


#class Reporte(models.Model)