from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *

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
# creaciom de funcion para cerra sesion
def logout(request):
    return logout_then_login(request, login_url="login")
# creaciom de funcion para redirigir y crear registro
def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request,'core/registro.html', {'form' :registro})