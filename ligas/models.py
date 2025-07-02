
from django.db import models
from django.contrib.auth.models import AbstractUser

class Deporte(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

class Federacion(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.ForeignKey('Deporte', on_delete=models.CASCADE, related_name='ligas')
    federacion = models.ForeignKey('Federacion', on_delete=models.CASCADE, related_name='ligas')
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=20, 
        choices=[('activa','Activa'),('inactiva','Inactiva'),('finalizada','Finalizada')]
    )

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    rol = models.CharField(
        max_length=30,
        choices=[
            ('admin_global', 'Admin Global'),
            ('federacion', 'Federación'),
            ('liga', 'Liga'),
            ('publico', 'Público'),
        ],
        default='publico'
    )
    federacion = models.ForeignKey('Federacion', on_delete=models.SET_NULL, null=True, blank=True)
