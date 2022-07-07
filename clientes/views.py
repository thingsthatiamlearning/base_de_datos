from django.shortcuts import render, redirect
#Se importan los clientes desde el archivo models.py
from .models import Cliente
from django.http import HttpResponse
#Se importa desde forms.py el clienteFormulario
from .forms import clienteFormulario
#Este import se utiliza para la barra de busqueda
from django.db.models import Q

#Se define el inicio el cual mostrara lo que hay en el inicio.html
def inicio(request):
    return render(request, 'paginas/inicio.html')

def funcion(request):
    return render(request, 'paginas/how_it_works.html')

#En el index se encuentra la barra de busqueda y todos los clintes
def index(request):
    #Aqui se le define como se llama la barra de busqueda en este caso "buscar"
    queryset = request.GET.get("buscar")
    print(queryset)
    #Esto es para que se muestren todos los clientes
    Clientes = Cliente.objects.all
    #Este if es para que se muestren los clientes ya sea que se introduzcan por nombre o numero de telefono. Estos nombres son los dados en el views.py
    if queryset:
        Clientes = Cliente.objects.filter(
            Q(Nombre__icontains = queryset) |
            Q(apellidoPaterno__icontains = queryset) |
            Q(apellidoMaterno__icontains = queryset) |
            Q(numeroTelefonico__icontains = queryset) |
            Q(id__icontains = queryset)
        ).distinct()
        #                                           ↓↓↓ Este nombre es el que se le pone en los html para los for
    return render(request, 'clientes/index.html', {'Clientes': Clientes})

#Para crear el cliente se trae lo creado en el formulario
def crearCliente(request):
    formulario = clienteFormulario(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
        #                                               ↓↓↓ nombre dado para usar en los for en html
    return render(request, 'clientes/crear.html', {'formulario': formulario})

#                           ↓ Para editar el cliente se solicita tambien el id del cliente
def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = clienteFormulario(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
    return render(request, 'clientes/editar.html',{'formulario': formulario})
#                      ↓ para eliminar al cliente tambien se pide el id 
def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista')


def noEncontrado(request, exception):
    return render(request, 'templates/noencontrado.html', status=404)