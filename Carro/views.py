from django.shortcuts import redirect, get_object_or_404, render
from TiendaApp.models import Producto
from .carro import Carro


# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
   # producto = Producto.objects.get(id=producto_id)
    carro.agregar_producto(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    #producto = Producto.objects.get(id=producto_id)
    carro.eliminar_producto(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    #producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto)
    return redirect("tienda")

def limpiar_carro(request):
    carro = Carro(request)  
    carro.limpiar_carro()
    return redirect("tienda")

