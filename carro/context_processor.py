def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        # se usa get() para evitar KeyError si 'carro' no está en la sesión
        carrito = request.session.get("carro", {})
        for key, value in carrito.items():
            total += float(value["precio"]) * value["unidades"]
    return {"importe_total_carro": total}
