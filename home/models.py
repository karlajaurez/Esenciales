from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Subcategoria(models.Model):
	nombre = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=300)
	descripcion = models.TextField()
	precio = models.DecimalField( max_digits=5, decimal_places=2)
	stock = models.IntegerField(default=0)
	modo_uso = models.TextField()
	imagen= models.ImageField(upload_to='products')
	subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

