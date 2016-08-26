from django.shortcuts import render
from home.models import *

def index(request):
	lista_categorias=Categoria.objects.all()
	slider = Slider.objects.all()
	return render(request, 'index.html',{'lista_categorias': lista_categorias, 'slider': slider})


