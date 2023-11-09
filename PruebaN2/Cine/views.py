from django.shortcuts import redirect, render
from Cine.models import Cine
from Cine.forms import registroCines


# Create your views here.

def Inicio(request):
    return render(request, 'Cine/index.html')

def registrarCine(request):
    form = registroCines()
    if request.method == 'POST' :
        form = registroCines(request.POST)
        if form.is_valid():
            form.save()
        return mostrar(request)
    data = {'form':form}
    return render(request, 'Cine/registrar.html',data)

def mostrar(request):
    cines = Cine.objects.all()
    data = {'cines':cines}
    return render(request, 'Cine/mostrar.html',data)

def mostrarActualizar(request):
    cines = Cine.objects.all()
    data = {'cines':cines}
    return render(request, 'Cine/actualizar.html',data)

def mostrarEliminar(request):
    cines = Cine.objects.all()
    data = {'cines':cines}
    return render(request, 'Cine/eliminar.html',data)

def actualizar(request, id):
    cine = Cine.objects.get(id = id)
    form = registroCines(instance = cine)
    if request.method == 'POST':
        form = registroCines(request.POST, instance = cine)
        if form.is_valid():
            form.save()
        return mostrar(request)
    data = {'form': form}
    return render(request, 'Cine/registrar.html',data)

def eliminar(request, id):
    cine = Cine.objects.get(id = id)
    cine.delete()
    return redirect('/mostrar')


