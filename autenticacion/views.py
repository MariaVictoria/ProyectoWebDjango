from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

class VRegistro(View):  
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'registro/registro.html', {'form':form})
    
    def post (self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("home")
        
        else: 
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'registro/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")


def login_view(request):
    return render(request, 'autenticacion/login.html')