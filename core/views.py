from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to= "login")
    carro = request.session.get("carro",[])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def carrito(request):
    #le vamos a pasar los productos que estan ingresados en el carrito.
    return render(request,'core/carrito.html', {"carro":request.session.get("carro",[])})

#creacion de sesion para usuario agregado de productos al carrito
def addtocar(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1 , producto.precio ])
    request.session["carro"] = carro
    return redirect(to= "home")

#creacion de sesion para usuario eliminar productos del carrito
def dropitem(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to= "carrito")

# limpia por cada cerrada de session el carrito
def limpiar(request):
    request.session.flush()
    return redirect(to= "home")

# Create your views here.
# creaciom de ruta hacia el archivo html 'principal.html'
def home(request):
    #le vamos a pasar los productos que estan ingresados en el db.
    dulces = Producto.objects.all()
    return render(request,'core/principal.html', {'dulces' :dulces, "carro":request.session.get("carro",[])})
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