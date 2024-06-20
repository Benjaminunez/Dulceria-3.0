from django.db import models

# Create your models here.

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
