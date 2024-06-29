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
]
