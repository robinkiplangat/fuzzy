from .models import Product
from .products import ProductIndex
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','type','category','code','ven', 'hfr','description','uom','price')
