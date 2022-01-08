from django.db import models

# Create your models here.
from django.db.models.fields.related import ForeignKey
from generaless.models import classModelo

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)

    #Se sugiere nombrar la clase en singular
    #No se deben indicar campos claves. Django genera en automitico la PrimaryKey

    def  __str__(self):
        return "%s" % ( self.nombre)

class Producto(classModelo):#aqui ya se ven los otros atributos en la herecia de modelos que se creo en la clase abtracta de generales classModelo
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField(default=0)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def  __str__(self):
         return "%s" % ( self.descripcion)

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    dirrecion=models.CharField(max_length=100)
    RFC=models.CharField(max_length=50)

    def  __str__(self):
         return "%s" % ( self.nombre)

class Venta(models.Model):
    fecha=models.DateField(max_length=50)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    
    def  __str__(self):
         return "%s" % ( self.fecha) 

class Detalles_Venta(models.Model):
    venta=models.ForeignKey(Venta,on_delete=models.CASCADE)
    produto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=0)
    costo_unitario=models.FloatField(default=0)

    
    def  __str__(self):
         return "%s" % ( self.cantidad)          