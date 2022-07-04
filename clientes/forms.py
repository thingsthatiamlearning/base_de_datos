#Para utilizar todos los campos de los clientes en el models.py
from django import forms
from .models import Cliente

class clienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'