from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre: ', unique=True, blank=False, help_text='Solo texto')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre: ', unique=True, blank=False)
    precio = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Precio: ', blank=False)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.RESTRICT)  # Aquí corregido

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, verbose_name='Cedula', unique=True, blank=False, null=False)
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre: ', unique=True, blank=False)
    apellido_cliente = models.CharField(max_length=50, verbose_name='Apellido: ', unique=True, blank=False)
    edad = models.IntegerField()
    correo = models.EmailField()
    domicilio = models.TextField(max_length=200, help_text='Escribe una indicación de tu domicilio')

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'

class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=4, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return f'Orden de {self.id} - Cliente {self.cliente.nombre_cliente}'
