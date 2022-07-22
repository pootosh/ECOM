from dataclasses import field
from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart')