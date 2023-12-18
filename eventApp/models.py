# Create your models here.
# en nombre_de_la_aplicacion/models.py

from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
