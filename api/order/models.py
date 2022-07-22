from statistics import mode
from django.db import models
from api.user.models import CustomUser
class Order(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    product_names = models.CharField(max_length=500, blank=True)
    transaction_id = models.CharField(max_length=150)
    total_amount = models.CharField(max_length=10, default=0)
    total_products = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
