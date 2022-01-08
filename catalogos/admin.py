from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Detalles_Venta,Producto, Venta

# Register your models here.

#admin.site.register(Categoria)

#admin.site.register(Producto)

#Se puede modiificar (str) el  orden de visulizacion utlizando el motodo  list_display()

class Categoria_Admin(admin.ModelAdmin):
    list_display=('nombre','descripcion')

admin.site.register(Categoria,Categoria_Admin)


class Producto_Admin(admin.ModelAdmin):
    list_display=('descripcion','precio','categoria')

admin.site.register(Producto,Producto_Admin)

class Cliente_Admin(admin.ModelAdmin):
    list_display=('nombre','dirrecion','RFC')
   
admin.site.register(Cliente,Cliente_Admin)

class Venta_Admin(admin.ModelAdmin):
    list_display=('fecha','cliente')
   
admin.site.register(Venta,Venta_Admin)

class Detalles_Venta_Admin(admin.ModelAdmin):
    list_display=('venta','produto','cantidad','costo_unitario')
   
admin.site.register(Detalles_Venta,Detalles_Venta_Admin)

