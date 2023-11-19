from django.shortcuts import redirect, render
from Funcion.models import Funcion
from Funcion.forms import registroFunciones


# Create your views here.

def Inicio(request):
    return render(request, 'Funcion/index.html')

def registrarFuncion(request):
    form = registroFunciones()
    if request.method == 'POST' :
        form = registroFunciones(request.POST)
        if form.is_valid():
            form.save()
        return mostrar(request)
    data = {'form':form}
    return render(request, 'Funcion/registrar.html',data)

def mostrar(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/mostrar.html',data)

def mostrarActualizar(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/actualizar.html',data)

def mostrarEliminar(request):
    funciones = Funcion.objects.all()
    data = {'funciones':funciones}
    return render(request, 'Funcion/eliminar.html',data)

def actualizar(request, id):
    funcion = Funcion.objects.get(id = id)
    form = registroFunciones(instance = funcion)
    if request.method == 'POST':
        form = registroFunciones(request.POST, instance = funcion)
        if form.is_valid():
            form.save()
        return mostrar(request)
    data = {'form': form}
    return render(request, 'Funcion/registrar.html',data)

def eliminar(request, id):
    funcion = Funcion.objects.get(id = id)
    funcion.delete()
    return redirect('/mostrar')