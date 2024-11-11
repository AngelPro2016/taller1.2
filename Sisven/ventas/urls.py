# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]

