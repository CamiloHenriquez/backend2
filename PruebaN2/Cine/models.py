from django.db import models
from django.core import validators
# Create your models here.

class Cine(models.Model):
    nombre = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    correo = models.EmailField(max_length=30)
    telefono = models.PositiveIntegerField(validators=[
        validators.MinValueValidator(911111111)
    ])
    cantSalas = models.PositiveIntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100000000000)
    ])
    aforo = models.PositiveIntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100000000000)
    ])

    def __str__(self) -> str:
        return self.nombre
