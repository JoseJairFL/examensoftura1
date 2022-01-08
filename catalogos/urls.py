from django.urls import path

from django.conf.urls import url

from . import views
from .views import CreateProducto, ListProducto, UpdateProducto

urlpatterns = [
    path('',views.home, name='home'),
    path('categorias/',views.categorias, name='categorias'),
    path('productos/',views.productos, name='productos'),


# RUTAS BASADAS EN FUNCIONES

#path('crear_producto/',views.crearProducto, name="crear_producto"),
#path('listar_producto/', views.listarProducto, name="listar_producto"),            
#url(r'^editar_producto/(?P<id>\d+)$',views.editarProducto,name="editar_producto"),

# TAREA 1 CREACION DE LA RUTA ELIMINAR BASADA EN FUNCIONES
#url(r'^eliminar_producto/(?P<id>\d+)$',views.eliminarProducto,name="eliminar_producto"),

    path('crear_producto/', CreateProducto.as_view(), name="crear_producto"),
    path('listar_producto/', ListProducto.as_view(), name="listar_producto"),
    path('editar_producto/<pk>',UpdateProducto.as_view(),name="editar_producto"),

# TAREA 2 CREACION DE LA RUTA ELIMINAR BASADA EN CLASES
path('eliminar_producto/<pk>',views.DeleteProducto.as_view(),name="eliminar_producto"),    
]