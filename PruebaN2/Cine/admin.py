from django.contrib import admin
from Cine.models import Cine

class CineAdmin(admin.ModelAdmin):
    list_display = ['nombre','ubicacion','correo','telefono','cantSalas','aforo']
# Register your models here.
admin.site.register(Cine,CineAdmin)
