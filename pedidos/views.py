# pedidos/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import logging

# Create your views here.

logger = logging.getLogger(__name__)
@login_required(login_url='/autenticacion/logear')

def procesar_pedido(request):
    logger.debug("Procesando pedido...")
    carro = Carro(request)

    if not carro.carro:
        messages.error(request, "El carrito está vacío.")
        return redirect('tienda')  # Redirect to the shopping page if the cart is empty


    if request.method == 'POST':
        pedido = Pedido.objects.create(user=request.user)
        lineas_pedido = []

    
        for key, value in carro.carro.items():
            lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['unidades'],
            user=request.user,  
            pedido=pedido

            ))

        LineaPedido.objects.bulk_create(lineas_pedido)

            # Limpiar el carrito después de procesar el pedido
        logger.debug("Limpiando el carrito...")
        carro.limpiar_carro()
        logger.debug("Carrito limpiado.")

    
        try:
            enviar_mail(
            pedido=pedido,
            lineas_pedido=lineas_pedido,
            nombreusuario=request.user.username,
            emailusuario=request.user.email,
            )
            logger.debug("Pedido creado con éxito.")
        except Exception as e:
            logger.error(f"Error al enviar el email: {e}")
            messages.error(request, "Hubo un problema al enviar el correo de confirmación.")


        messages.success(request, "El pedido se ha creado con exito")

        return redirect ('tienda')
    
    return redirect('carro')

def enviar_mail(**kwargs):
    try:
        asunto='Gracias por su pedido. Tienda Django María Victoria.'
        mensaje= render_to_string('emails/pedido.html', {
            'pedido': kwargs.get('pedido'),
            'lineas_pedido': kwargs.get ('lineas_pedido'),
            'nombreusuario': kwargs.get('nombreusuario'),
            
        })

        mensaje_texto=strip_tags(mensaje)
        from_email='maria.victoria.webdev@gmail.com'
        to=kwargs.get('emailusuario')
        # Add logging for debugging
        print(f"Sending email to {to}...")

        send_mail(
            asunto,
            mensaje_texto,
            from_email,
            [to],
            html_message=mensaje
        )
        logger.debug("Email enviado con éxito.")
    
    except Exception as e:
       logger.error(f"Error al enviar el email: {e}")
    