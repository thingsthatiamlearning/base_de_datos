from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    #Aqui se le dice a la aplicacion que incluya los urls agregados en clientes.urls.py
    path('', include('clientes.urls'))
]
