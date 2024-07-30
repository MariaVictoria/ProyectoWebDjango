from django.urls import path
from TiendaApp import views
from TiendaApp.models import Producto



urlpatterns = [
    
    path('', views.tienda, name='tienda'), 
]
