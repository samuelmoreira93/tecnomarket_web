from .models import Producto,Marca
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Marca
        fields='__all__'


class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca=serializers.CharField(read_only=True, source='marca.nombre')
    marca=MarcaSerializer(read_only=True)
    class Meta:
        model=Producto
        fields='__all__'