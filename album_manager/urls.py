# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('artistas/', views.lista_artistas, name='lista_artistas'),
    path('albumes/', views.lista_albumes, name='lista_albumes'),
    path('artistas/', views.lista_artistas, name='lista_artistas'),
    path('artista/<int:pk>/', views.detalle_artista, name='detalle_artista'),
    path('artista/nuevo/', views.crear_artista, name='crear_artista'),
    path('artista/<int:pk>/editar/', views.editar_artista, name='editar_artista'),
    path('artista/<int:pk>/eliminar/', views.eliminar_artista, name='eliminar_artista'),
    path('albumes/', views.lista_albumes, name='lista_albumes'),
    path('album/<int:pk>/', views.detalle_album, name='detalle_album'),
    path('album/nuevo/', views.crear_album, name='crear_album'),
    path('album/<int:pk>/editar/', views.editar_album, name='editar_album'),
    path('album/<int:pk>/eliminar/', views.eliminar_album, name='eliminar_album'),
]