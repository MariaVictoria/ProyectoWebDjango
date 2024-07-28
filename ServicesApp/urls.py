from django.urls import path
from ServicesApp import views

urlpatterns = [
    path('', views.servicios, name='servicios'),  
]
