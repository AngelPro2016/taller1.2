from django.contrib import admin
from .models import Categorias,Cliente,Orden,Producto
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Orden)
admin.site.register(Producto)
admin.site.register(Cliente)
