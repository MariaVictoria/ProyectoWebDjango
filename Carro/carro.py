import logging

logger = logging.getLogger(__name__)

class Carro:
    def __init__(self, request):
        self.request = request  
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
                logger.debug("Creating new cart in session.")
                self.carro = self.session['carro'] = {}
        else:
            self.carro = carro
            
        logger.debug(f"Cart loaded: {self.carro}")


    def agregar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'imagen': producto.imagen.url,
                'disponibilidad': producto.disponibilidad,
                'unidades': 1
            }
            logger.debug(f"Added new product: {self.carro[producto_id]}")

        else:
            self.carro[producto_id]['unidades'] += 1
            self.carro[producto_id]['precio'] = self.carro[producto_id]['unidades'] * float(producto.precio)
            logger.debug(f"Updated product: {self.carro[producto_id]}")
    
        '''else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['unidades'] += 1
                    
                    value['precio'] = value['unidades'] * float(producto.precio)
                    break'''

        self.guardar_carro()
        return True

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        logger.debug("Cart saved to session.")

    def eliminar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
                del self.carro[producto_id]
                self.guardar_carro()
                logger.debug(f"Removed product {producto_id} from cart.")

    def restar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            value = self.carro[producto_id]
            value['unidades'] -= 1
            if value['unidades'] < 1:
                self.eliminar_producto(producto)
            else:
                value['precio'] = value['unidades'] * float(producto.precio)
                self.guardar_carro()
                logger.debug(f"Reduced quantity of product {producto_id} in cart.")


    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
        logger.debug("Cart cleared.")

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def calcular_total_carro(self):
        total = 0
        for key, value in self.carro.items():
            total += float(value['precio'])
        logger.debug(f"Total cart value calculated: {total}")
        return total