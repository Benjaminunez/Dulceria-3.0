from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey( to= User, on_delete= models.CASCADE)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:20]

class Producto (models.Model):
    codigo = models.CharField(max_length= 4, primary_key= True)
    detalle = models.CharField(max_length= 300)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200) # permite agregar la ruta de la imagen

    
    def tachado(self):
        if self.oferta:
            return "$"+str(round(self.precio * (1.2)))
        return ""
    
    #metodo para que en el menu admin no aparesca por defecto "product object" en producto
    def __str__(self):
        return self.detalle+" ("+self.codigo+")"

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta , on_delete= models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.producto.detalle[0:12]+" "+str(self.venta.id)
