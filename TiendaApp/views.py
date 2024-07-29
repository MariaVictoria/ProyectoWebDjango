from django.shortcuts import render
from .models import CategoriaProducto, Producto
# Create your views here.

def tienda (request):

    productos=Producto.objects.all()

    return render(request, 'TiendaApp/tienda.html', {'productos':productos})



