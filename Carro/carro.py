class Carro:
    def __init__(self, request):
        self.request = request  
        self.session = request.session
        carro=self.session.get('carro')
        if not carro:
            carro=self.session['carro'] = {}
         

        else:
            self.carro = carro

def agregar (self, producto):
    if(str(producto.id) not in self.carro.keys()):
        self.carro[producto.id] = {
            'producto_id': producto.id,
            'nombre':producto.nombre,
            'precio': str(producto.precio),
            'imagen': producto.imagen.url,
            'disponibilidad':producto.disponibilidad,
            'unidades': 1
        }

    else:
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['unidades'] = value['unidades'] + 1   
                break

    self.guardar_carro()
    return True


def guardar_carro(self):
    self.session['carro'] = self.carro
    self.session.modified = True

def eliminar(self, producto):
    if(str(producto.id) in self.carro):
        del self.carro[producto.id]

        self.guardar_carro()
        

def restar_producto(self, producto):
    for key, value in self.carro.items():
        if key == str(producto.id):
            value['unidades'] = value['unidades'] - 1   
            break

    self.guardar_carro()

