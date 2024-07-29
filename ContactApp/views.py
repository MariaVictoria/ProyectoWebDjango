from django.shortcuts import render, HttpResponseRedirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto (request):
    formulario_contacto=FormularioContacto()
    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            mensaje=request.POST.get('mensaje')

            email=EmailMessage(
                'Mensaje de contacto web Django',
                'El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}'.format(nombre, email, mensaje),
                '',
                ['maria.victoria.webdev@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return HttpResponseRedirect('/contacto/?valido')
            except:
                return HttpResponseRedirect('/contacto/?novalido')
            
    return render(request, 'ContactApp/contacto.html', {'mi_formulario': formulario_contacto})

