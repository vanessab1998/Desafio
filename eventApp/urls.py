from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/', views.ListaEventos.as_view(), name='lista-eventos'),
    path('eventos/<int:pk>/', views.DetalleEvento.as_view(), name='detalle-evento'),
    path('enlistar/', views.enlistar, name="enlistar"),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit_event'),
]

