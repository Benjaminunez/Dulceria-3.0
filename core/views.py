from django.shortcuts import render
from .models import *

# Create your views here.
# creaciom de ruta hacia el archivo html 'principal.html'
def home(request):
    #le vamos a pasar los productos que estan ingresados en el db.
    dulces = Producto.objects.all()
    return render(request,'core/principal.html', {'dulces' :dulces})
# creaciom de ruta hacia el archivo html 's.nosotros.html'
def nosotros(request):
    return render(request,'core/s.nosotros.html')
# creaciom de ruta hacia el archivo html 'colaboradores'
def colaborador(request):
    return render(request,'core/colaborador.html')
# creaciom de ruta hacia el archivo html 'contactos'
def contacto(request):
    return render(request,'core/contactos.html')
