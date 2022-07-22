from django.db import models
from api.user.models import CustomUser
from api.order.models import Order
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.JSONField(serialize=True, null=True, blank=True)
    
    # def __str__(self):
    #     return self.user