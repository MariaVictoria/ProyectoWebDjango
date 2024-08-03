from django.shortcuts import render
from ServicesApp.models import Servicio

def servicios (request):
    servicios=Servicio.objects.all()
    return render(request, 'ServicesApp/servicios.html', {'servicios':servicios})