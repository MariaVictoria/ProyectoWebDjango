
from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path ('home/', views.home, name='home'),
    path ('services/', views.services, name='services'),
    path('tienda/', views.tienda, name='tienda'),
    path('contact/', views.contact, name='contact'),
    path ('blog/', views.blog, name='blog'),
]
