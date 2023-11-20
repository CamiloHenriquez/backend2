from django.shortcuts import redirect, render
from Sala.models import Sala
from Sala.forms import registroSalas

# Create your views here.

def registrarSala(request):
    form = registroSalas()
    if request.method == 'POST' :
        form = registroSalas(request.POST)
        if form.is_valid():
            form.save()
        return mostrarSala(request)
    data = {'form':form}
    return render(request, 'Sala/registrarSala.html',data)

def mostrarSala(request):
    salas = Sala.objects.all()
    data = {'salas':salas}
    return render(request, 'Sala/mostrarSala.html',data)

def mostrarActualizarSala(request):
    salas= Sala.objects.all()
    data = {'salas':salas}
    return render(request, 'Sala/actualizarSala.html',data)

def mostrarEliminarSala(request):
    salas = Sala.objects.all()
    data = {'salas':salas}
    return render(request, 'Sala/eliminarSala.html',data)

def actualizarSala(request, id):
    sala = Sala.objects.get(id = id)
    form = registroSalas(instance = sala)
    if request.method == 'POST':
        form = registroSalas(request.POST, instance = sala)
        if form.is_valid():
            form.save()
        return mostrarSala(request)
    data = {'form': form}
    return render(request, 'Sala/registrarSala.html',data)

def eliminarSala(request, id):
    sala = Sala.objects.get(id = id)
    sala.delete()
    return redirect('/mostrarSala')
