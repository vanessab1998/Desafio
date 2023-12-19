from asyncio import events
from os import abort

from click import Abort
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import requests
from rest_framework import generics
from django.contrib import messages
from eventApp import apps
from .models import Evento
from .serializers import EventoSerializer

def index(request):
    return render(request, 'index.html')

class ListaEventos(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class DetalleEvento(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

def enlistar(request):
    return render(request, 'enlistar.html')

def edit_event(request):
    return render(request, 'edit_event.html')

def lista_eventos(request):
    eventos = Evento.objects.all()
    context = {
        'eventos': eventos,
    }
    return render(request, 'lista_eventos.html', context)

def eliminar_evento(request, evento_id): #ELIMINAR Evento
    horaMed = get_object_or_404(Evento, id=evento_id)
    horaMed.delete()
    messages.success(request, "Eliminado correctamente")
 
    return redirect(to="lista_eventos")