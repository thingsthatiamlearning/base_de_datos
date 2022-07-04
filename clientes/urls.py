from cgitb import handler
from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('lista', views.index, name='lista'),
    path('crear', views.crearCliente, name='crear'),
    path('editar', views.editarCliente, name='editar'),
    path('funcion', views.funcion, name='funcion'),

    path('editar/<int:id>', views.editarCliente, name='editar'),
    path('elimiar/<int:id>', views.eliminar, name='eliminar'),
]

handler404 = "clientes.views.noEncontrado"