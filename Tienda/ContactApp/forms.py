from django import forms
import random

# Generar números aleatorios
num1 = random.randint(1, 30)
num2 = random.randint(1, 10)
suma = num1 + num2

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)

''' captcha_answer = forms.IntegerField(label=f"{num1} + {num2}", label_suffix=" =", required=True)

    def clean_captcha_answer(self):
        captcha_answer = self.cleaned_data["captcha_answer"]
        if captcha_answer != suma:
            raise forms.ValidationError("Respuesta incorrecta.")'''
