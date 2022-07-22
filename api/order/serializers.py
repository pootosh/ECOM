from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'transaction_id', 'total_products', 'total_amount')