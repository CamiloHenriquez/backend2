from django.contrib import admin
from Funcion.models import Funcion

class FuncionAdmin(admin.ModelAdmin):
    list_display = ['duracionFuncion','nombreFuncion','horarioFuncion','tipoFuncion','generoFuncion','restriccionEdad']
# Register your models here.
admin.site.register(Funcion,FuncionAdmin)
