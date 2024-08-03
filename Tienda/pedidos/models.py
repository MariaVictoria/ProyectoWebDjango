from django.db import models
from django.contrib.auth import get_user_model 
from TiendaApp.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model() #devuelve el usuario logeado

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('precio') * F('cantidad'), output_field=FloatField)
        )['total'] or 0

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        managed = True
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']
    
    @property
    def total(self):
        return self.cantidad * self.producto.precio

    '''@property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('producto__precio') * F('cantidad'), output_field=FloatField)
        )['total'] or 0
'''