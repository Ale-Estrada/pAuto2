# saludos/urls.py

from django.urls import path
from . import views # Importamos las vistas de nuestra app

urlpatterns = [
    # Cuando la URL esté vacía (''), ejecuta la función views.hola_mundo
    path('', views.generador_carta, name='generador_carta'),
]