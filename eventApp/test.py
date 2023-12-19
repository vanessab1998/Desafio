# tests.py
from django.test import TestCase
from datetime import date
from .models import Evento

class EventoTestCase(TestCase):
    def setUp(self):
        # Configuramos datos de prueba
        self.evento = Evento.objects.create(
            titulo='Evento de Prueba',
            descripcion='Este es un evento de prueba.',
            fecha=date.today(),
            ubicacion='Vitacura',
        )

    def test_creacion_evento(self):
        # Verificamos que el evento se haya guardado correctamente en la base de datos
        evento_recuperado = Evento.objects.get(pk=self.evento.id)
        self.assertEqual(evento_recuperado.titulo, 'Evento de Prueba')
        self.assertEqual(evento_recuperado.descripcion, 'Este es un evento de prueba.')
        self.assertEqual(evento_recuperado.fecha, date.today())
        self.assertEqual(evento_recuperado.ubicacion, 'Vitacura')

    def test_str_method(self):
        # Verificamos que el método __str__ del modelo funcione como se espera
        self.assertEqual(str(self.evento), 'Evento de Prueba')

