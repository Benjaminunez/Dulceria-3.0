
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= "home"), # url de pagina principal 
    path('nosotros',nosotros, name= "nosotros"), # url de pagina sobre nosotros
    path('colaborador',colaborador, name= "colaborador"), # url de pagina colaboradores
    path('contacto',contacto, name= "contacto"), # url de pagina contactos
]
