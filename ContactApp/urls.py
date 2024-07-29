from django.urls import path
from ContactApp import views

urlpatterns = [
    path('', views.contacto, name='contacto'),  
]
