
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Producto
from catalogos.forms import ProductoForm

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

#Adicional
from .models import Categoria

# Create your views here.
def home(request):
    return render(request, 'home.html')

def categorias(request):
   # return render(request, 'categorias.html')
   # uso de los Query Set de Django - Consultas ala base de datos me diante el ORM
   categ = Categoria.objects.all().order_by('nombre') #Select * from categorias
   contexto = {'categorias' : categ}
   return render (request, 'categorias.html', contexto)

def productos(request):
    return render(request, 'productos.html')


# VISTAS BASADAS EN FUNCIONES 

def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = ProductoForm()
    return render (request, 'crear_producto.html', {'form':form})

def listarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render (request, 'listar_producto.html', contexto)

def editarProducto(request,id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect ('home')
    return render (request, 'crear_producto.html', {'form' : form})

    # TAREA 1 CRERACION DE LA VISTA PARA ELIMINAR

def eliminarProducto(request, id):# Para editar un produto
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('home')
    
   
    # VISTAS BASADAS EN CLASES

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('listar_producto')

class ListProducto(ListView):
    model = Producto
    template_name = "listar_producto.html"
    
class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('home')

 # TAREA 2 CRERACION DE LA VISTA PARA ELIMINAR

class DeleteProducto(DeleteView):
    model = Producto
    template_name = "producto_confirm_delete.html"
    success_url = reverse_lazy('listar_producto')

    