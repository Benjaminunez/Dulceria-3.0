
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name= "home"), # url de pagina principal
    path('login', LoginView.as_view(template_name='core/login.html'), name= "login"), # url de pagina Login
    path('nosotros',nosotros, name= "nosotros"), # url de pagina sobre nosotros
    path('colaborador',colaborador, name= "colaborador"), # url de pagina colaboradores
    path('contacto',contacto, name= "contacto"), # url de pagina contactos
    path('registro',registro,name="registro"), #url para el registro de nuevos usuarios
    path('addtocar/<codigo>',addtocar,name="addtocar"), #url para el registro productos carrito
    path('dropitem/<codigo>',dropitem,name="dropitem"), #url para el eliminar productos carrito
    path('limpiar',limpiar), #url para limpiar carrito
    path('carrito',carrito,name="carrito"), #url para carrito
    path('comprar',comprar,name="comprar"), #url para carrito
]