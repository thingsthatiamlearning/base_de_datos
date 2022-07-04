from tabnanny import verbose
from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from distutils.command.upload import upload

class Cliente(models.Model):
    id                      = models.AutoField(primary_key=True)
    Nombre                  = models.CharField(max_length=20, verbose_name="Nombre")
    apellidoPaterno         = models.CharField(max_length=20, verbose_name="Apellido Paterno", default="")
    apellidoMaterno         = models.CharField(max_length=20, verbose_name="Apellido Materno", default="")
    nacimiento              = models.DateField(verbose_name="Nacimiento: dd/mm/yyyy")
    correoElectronico       = models.EmailField(max_length=200, verbose_name="Correo", blank=True)
    numeroTelefonico        = PhoneNumberField(unique = True, null = False, blank = False, verbose_name='Numero de telefono')
    vivienda                = models.CharField(max_length=100, verbose_name="Lugar Donde Vive")
    nota                    = models.TextField(verbose_name="nota", blank=True)

    def __str__(self):
        fila = "Nombre: " + self.Nombre + " - " + "Numero de telefono: " + str(self.numeroTelefonico)
        return fila
