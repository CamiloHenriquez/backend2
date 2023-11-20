from django.shortcuts import redirect, render
from Funcion.models import Funcion
from Funcion.forms import registroFunciones


# Create your views here.

def registrarFuncion(request):
    form = registroFunciones()
    if request.method == 'POST' :
        form = registroFunciones(request.POST)
        if form.is_valid():
            form.save()
        return mostrarFuncion(request)
    data = {'form':form}
    return render(request, 'Funcion/registrarFuncion.html',data)

def mostrarFuncion(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/mostrarFuncion.html',data)

def mostrarActualizarFuncion(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/actualizarFuncion.html',data)

def mostrarEliminarFuncion(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/eliminarFuncion.html',data)

def actualizarFuncion(request, id):
    funcion = Funcion.objects.get(id = id)
    form = registroFunciones(instance = funcion)
    if request.method == 'POST':
        form = registroFunciones(request.POST, instance = funcion)
        if form.is_valid():
            form.save()
        return mostrarFuncion(request)
    data = {'form': form}
    return render(request, 'Funcion/registrarFuncion.html',data)

def eliminarFuncion(request, id):
    funcion = Funcion.objects.get(id = id)
    funcion.delete()
    return redirect('/mostrarFuncion')