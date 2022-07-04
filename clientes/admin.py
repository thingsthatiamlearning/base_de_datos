from encodings import search_function
from django.contrib import admin

from .models import Cliente
from clientes.models import Cliente

class clienteadmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'correoElectronico', 'numeroTelefonico', 'vivienda')
    search_fields = ['Nombre', 'correoElectronico']

admin.site.register(Cliente, clienteadmin)