from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Product
        fields = ('id','name', 'description', 'price', 'image', 'category')