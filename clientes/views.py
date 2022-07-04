from django.shortcuts import render, redirect
from .models import Cliente
from django.http import HttpResponse
from .forms import clienteFormulario
from django.db.models import Q

def inicio(request):
    return render(request, 'paginas/inicio.html')

def funcion(request):
    return render(request, 'paginas/how_it_works.html')

def index(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    Clientes = Cliente.objects.all
    if queryset:
        Clientes = Cliente.objects.filter(
            Q(Nombre__icontains = queryset) |
            Q(id__icontains = queryset)
        ).distinct()
    return render(request, 'clientes/index.html', {'Clientes': Clientes})

def crearCliente(request):
    formulario = clienteFormulario(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
    return render(request, 'clientes/crear.html', {'formulario': formulario})

def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = clienteFormulario(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
    return render(request, 'clientes/editar.html',{'formulario': formulario})

def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista')


def noEncontrado(request, exception):
    return render(request, 'templates/noencontrado.html', status=404)