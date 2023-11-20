from django.db import models
from django import forms
from Cine.models import Cine
from django.core import validators

# Create your models here.
inclusividad=[
    ("si","Si"),
    ("no","No"),
]

tiposalaChoice=[
    ("normal","Normal"),
    ("premiun","Premiun"),
    ("vip","Vip")
]
estadosalaChoice=[
    ("disponible","Disponible"),
    ("ocupado","Ocupado"),
]

tamanioPantallaChoice = [
    ("50","50"),
    ("55","55"),
    ("60","60"),
    ("65","65"),
    ("70","70"),
    ("80","80"),
]


class Sala(models.Model):
    CantidadSilla=models.PositiveIntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100000000000000000000000000)
    ])
    NumeroSala=models.PositiveIntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(100000000000000000000000000)
    ])
    TamanioPantalla=models.CharField(max_length=10, choices=tamanioPantallaChoice)
    InclusividadSala=models.CharField(max_length=4, choices= inclusividad)
    TipoSala=models.CharField(max_length=10,choices=tiposalaChoice)
    EstadoSala=models.CharField(max_length=10,choices=estadosalaChoice)
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.NumeroSala}'