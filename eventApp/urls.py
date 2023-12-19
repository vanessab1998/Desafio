from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/', views.ListaEventos.as_view(), name='lista-eventos'),
    path('eventos/<int:pk>/', views.DetalleEvento.as_view(), name='detalle-evento'),
    path('enlistar/', views.enlistar, name="enlistar"),
    path('edit_event/', views.edit_event, name='edit_event'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
    path('eliminar_evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
]

