from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.models import User

# Define the custom user creation form
class CustomUserCreationForm(UserCreationForm):
    emailusuario = forms.EmailField(required=True, label="Email")
    emailusuario_confirm = forms.EmailField(required=True, label="Confirm Email")

    class Meta:
        model = User
        fields = ("username", "emailusuario", "emailusuario_confirm", "password1", "password2")

    def clean_email_confirm(self):
        emailusuario = self.cleaned_data.get('email')
        emailusuario_confirm = self.cleaned_data.get('email_confirm')

        if emailusuario != emailusuario_confirm:
            raise forms.ValidationError("Emails don't match")

        return emailusuario_confirm

# View for user registration
class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'registro/registro.html', {'form': form})

# View to log out
def cerrar_sesion(request):
    logout(request)
    return redirect("home")

# View to log in
def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=nombre_usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})
