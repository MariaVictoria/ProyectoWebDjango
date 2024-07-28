from django.shortcuts import render, HttpResponse
from Services.models import Servicio

# Create your views here.

def home (request):
    return render(request, 'ProyectoWebApp/home.html', {})



def tienda (request):
    return render(request, 'ProyectoWebApp/tienda.html', {})



def contact (request):
    return render(request, 'ProyectoWebApp/contact.html', {})