from django.db import models
from django.core import validators
from Sala.models import Sala
# Create your models here.

tipoFuncionChoice=[
    ("3D","3D"),
    ("2D","2D")
]

edadFuncionChoice=[
    ("mayor de edad","+18"),
    ("TE","Todo espectador"),
    ("mayor de 14","14")
]

class Funcion(models.Model):
    duracionFuncion = models.CharField(max_length=20)
    nombreFuncion = models.CharField(max_length=20)
    horarioFuncion= models.CharField(max_length=30)
    tipoFuncion = models.CharField(max_length=10, choices= tipoFuncionChoice)
    generoFuncion = models.CharField(max_length=30)
    restriccionEdad = models.CharField(max_length=30, choices=edadFuncionChoice)
    sala = models.ForeignKey(Sala, on_delete= models.CASCADE)

