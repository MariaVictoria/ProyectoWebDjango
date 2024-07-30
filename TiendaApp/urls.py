from django.urls import path
from TiendaApp import views



urlpatterns = [
    
    path('', views.tienda, name='tienda'), 
]
