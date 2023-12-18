from django.shortcuts import render
from rest_framework import generics
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
