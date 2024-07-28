
from django.urls import path
from ContactApp import views


urlpatterns = [
  
    path('contacto/', views.contacto, name='contacto'),
    
]

