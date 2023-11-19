from django.contrib import admin
from Sala.models import Sala

class SalaAdmin(admin.ModelAdmin):
    list_display = ['CantidadSilla','NumeroSala','TamanioPantalla','InclusividadSala','TipoSala','EstadoSala']
# Register your models here.
admin.site.register(Sala,SalaAdmin)
