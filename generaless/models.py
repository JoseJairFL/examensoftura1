from abc import abstractstaticmethod
from django.db import models

# se crea una clase de modelo anstracta que se heredara a otros modelos en otras aplicaciones 

class classModelo(models.Model):
    activo=models.BooleanField(default=True)
    creado=models.DateField(auto_now_add=True)#en automatico en la que se crea
    modificado=models.DateField(auto_now=True)

    class Meta: #la clase abstracta
        abstract=True