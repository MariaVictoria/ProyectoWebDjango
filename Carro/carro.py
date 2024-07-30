class Carro:
    def __init__(self, request):
        self.request = request  
        self.session = request.session
        carro=self.session.get('carro')
        if not carro:
            carro=self.session['carro'] = {}
         

        else:
            self.carro = carro

    def agregar_producto(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'imagen': producto.imagen.url,
                'disponibilidad': producto.disponibilidad,
                'unidades': 1
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['unidades'] += 1
                    value['precio'] = value['unidades'] * float(producto.precio)
                    break

        self.guardar_carro()
        return True


    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar_producto(self, producto):
        if(str(producto.id) in self.carro):
            del self.carro[producto.id]

            self.guardar_carro()
            

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['unidades'] = value['unidades'] - 1   
                if value['unidades'] < 1:
                    self.eliminar_producto(producto)
                break

        self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
        