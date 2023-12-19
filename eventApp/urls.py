from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/', views.ListaEventos.as_view(), name='lista-eventos'),
    path('eventos/<int:pk>/', views.DetalleEvento.as_view(), name='detalle-evento'),
    path('enlistar/', views.enlistar, name="enlistar"),
]

