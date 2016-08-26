from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Subcategoria(models.Model):
	nombre = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	precio = models.DecimalField( max_digits=5, decimal_places=2)
	stock = models.IntegerField(default=0)
	modo_uso = models.TextField()
	imagen= models.ImageField(upload_to='products')
	subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nombre

class Slider(models.Model):
	titulo=models.CharField(max_length=300)
	#tamano de imagen 1920 x 700
	imagen=models.ImageField(upload_to='slider')
	descripcion=models.CharField(max_length=300)
	descripcion_corta=models.CharField(max_length=40, blank=True)
	active=models.BooleanField(default=True, verbose_name='Imagen Activa')
	link=models.CharField(max_length=500, blank=True)
	titulo_link = models.CharField(max_length=20, blank=True)
	
	def __str__(self):
		return self.titulo


