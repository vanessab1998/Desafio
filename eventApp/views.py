from asyncio import events
from os import abort
from click import Abort
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from rest_framework import generics

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


from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

from django.shortcuts import render, get_object_or_404
from .models import Evento
from .forms import EventForm

def edit_event(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lista-eventos/')
    else:
        form = EventForm(instance=evento)

    return render(request, 'edit_event.html', {'form': form, 'evento': evento})


