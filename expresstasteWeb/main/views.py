from django.shortcuts import render
from django.http import HttpResponse

from . models import Usuario, Categoria, Producto, TipoNegocio, Negocio, EstadoPedido, Mesa, Pedido, DetallePedido, Rol
from . serializers import UsuarioSerializer, CategoriaSerializer, ProductoSerializer, NegocioSerializer, TipoNegocioSerializer, MesaSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer, RolSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def inicio(request):
    return HttpResponse('ksajdkasjdkas')



# API
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

class TipoNegocioViewSet(viewsets.ModelViewSet):
    queryset = TipoNegocio.objects.all()
    serializer_class = TipoNegocioSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer