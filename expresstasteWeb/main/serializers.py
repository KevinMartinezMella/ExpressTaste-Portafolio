from rest_framework import serializers
from . models import Usuario, Categoria, Producto, Negocio, TipoNegocio, EstadoPedido, Mesa, Pedido, DetallePedido, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNegocio
        fields = '__all__'

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['mesa', 'estado', 'usuario']

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'