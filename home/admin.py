from django.contrib import admin
from .models import *


class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'active')

admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Slider, SliderAdmin)