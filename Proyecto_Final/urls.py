from django.urls import path
from Proyecto_Final import views


urlpatterns = [
    path('corredores/', views.ListadoCorredores.as_view(), name='listado_corredores'),
    path('crear-corredores/', views.CrearCorredores.as_view(), name='crear_corredores'),
    path('editar-corredores/<int:pk>/', views.EditarCorredores.as_view(), name='editar_corredores'),
    path('eliminar-corredores/<int:pk>/', views.EliminarCorredores.as_view(), name='eliminar_corredores'),
    path('mostrar-corredores/<int:pk>/', views.MostrarCorredores.as_view(), name='mostrar_corredores'),
    path('carreras/', views.ListadoCarreras.as_view(), name='listado_carreras'),
    path('crear-carreras/', views.CrearCarreras.as_view(), name='crear_carreras'),
    path('editar-carreras/<int:pk>/', views.EditarCarreras.as_view(), name='editar_carreras'),
    path('eliminar-carreras/<int:pk>/', views.EliminarCarreras.as_view(), name='eliminar_carreras'),
    path('mostrar-carreras/<int:pk>/', views.MostrarCarreras.as_view(), name='MostrarCarreras'),
    path('', views.home, name='home'),
    path('index/', views.home, name='home'),
]