# Serialzador: es una clase que se encarga de traducir los modelos de Django a un formato que puede ser enviado atravez de la app
#pueden ser datos JSON
#puede valir datos y transformarlos a datos de api


from rest_framework import serializers
from .models import Product, Category

#creacion de serializador

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'