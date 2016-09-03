from django.shortcuts import render
from home.models import *
from django.views.generic import ListView

def index(request):
	lista_categorias=Categoria.objects.all()
	slider = Slider.objects.all()
	return render(request, 'index.html',{'lista_categorias': lista_categorias, 'slider': slider})


# def lista_productos(request):
# 	lista_productos = Producto.objects.all()
# 	return render(request, 'productos.html',{'lista_productos': lista_productos})


class ProductoView(ListView):
	template_name = 'productos.html'
	model = Producto
	context_object_name = 'lista_productos'