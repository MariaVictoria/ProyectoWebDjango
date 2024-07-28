from django.shortcuts import render
from Services.models import Servicio

def servicios (request):
    servicios=Servicio.objects.all()
    return render(request, 'Services/services.html', {'servicios':servicios})