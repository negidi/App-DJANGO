"""ProyectoEjemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appgestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_todo/',views.listar_todo),
    path('listar_todo_articulos/',views.listar_todo_articulos),
    path('ingresar_productos/', views.ingresar_productos),
    path('ingreso_producto/',views.ingreso_producto),
    path('busqueda_productos/',views.busqueda_productos),
    path('buscar/',views.buscar),
    path('eliminar_producto/',views.eliminar_producto),
    path('eliminacion_producto/',views.eliminacion_producto),
    path('modificar_articulo/',views.modificar_articulo),
    path('modificar/',views.modificar),
    path('index/',views.index),
]
