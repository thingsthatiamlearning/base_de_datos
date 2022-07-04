from encodings import search_function
from django.contrib import admin

from .models import Cliente
from clientes.models import Cliente

#Clase para que se muestre los datos del cliente en el modo admin
class clienteadmin(admin.ModelAdmin):
    #Para que se muestren estos datos  en el admin
    list_display = ('id', 'Nombre', 'correoElectronico', 'numeroTelefonico', 'vivienda')
    #Para que se pueda buscar en el modo admin por nombre y correo
    search_fields = ['Nombre', 'correoElectronico']

admin.site.register(Cliente, clienteadmin)