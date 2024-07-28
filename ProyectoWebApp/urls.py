
from django.urls import path
from ProyectoWebApp import views


urlpatterns = [
    path ('home/', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('contact/', views.contact, name='contact'),
    
]

