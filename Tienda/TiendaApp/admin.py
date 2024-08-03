from django.contrib import admin
from . models import CategoriaProducto, Producto

# Register your models here.
class CategoriasProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProducto,CategoriasProductoAdmin)

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Producto, ProductosAdmin)