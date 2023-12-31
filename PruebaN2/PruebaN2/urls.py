"""
URL configuration for PruebaN2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Cine import views
from Funcion import views as Funciones 
from Sala import views as Salas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio),
    path('mostrar', views.mostrar),
    path('registrarCine', views.registrarCine),
    path('actualizar/<int:id>', views.actualizar),
    path('eliminar/<int:id>', views.eliminar),
    path('mostrarActualizar', views.mostrarActualizar),
    path('mostrarEliminar', views.mostrarEliminar),

    path('registrarFuncion', Funciones.registrarFuncion),
    path('mostrarFuncion', Funciones.mostrarFuncion),
    path('actualizarFuncion/<int:id>', Funciones.actualizarFuncion),
    path('eliminarFuncion/<int:id>', Funciones.eliminarFuncion),
    path('mostrarActualizarFuncion', Funciones.mostrarActualizarFuncion),
    path('mostrarEliminarFuncion', Funciones.mostrarEliminarFuncion),

    path('registrarSala', Salas.registrarSala),
    path('mostrarSala', Salas.mostrarSala),
    path('actualizarSala/<int:id>', Salas.actualizarSala),
    path('eliminarSala/<int:id>', Salas.eliminarSala),
    path('mostrarActualizarSala', Salas.mostrarActualizarSala),
    path('mostrarEliminarSala', Salas.mostrarEliminarSala),
]
