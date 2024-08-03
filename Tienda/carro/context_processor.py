import logging

logger = logging.getLogger(__name__)

def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get('carro', {})
        logger.debug(f"Carro en sesión: {carro}")
        for key, value in carro.items():
            precio = value.get("precio", 0)
    
            try:
                total += float(precio)
            except ValueError:
                logger.warning(f"Precio no convertible a float: {precio}")
    else:
        total='Inicia sesión para ver el importe total'

    return {"importe_total_carro": total}
