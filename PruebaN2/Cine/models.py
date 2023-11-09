from django.db import models

# Create your models here.

class Cine(models.Model):
    nombre = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    correo = models.EmailField(max_length=30)
    telefono = models.IntegerField()
    cantSalas = models.IntegerField()
    aforo = models.IntegerField()


