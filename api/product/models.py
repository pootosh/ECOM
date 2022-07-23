import os
from django.db import models
from api.category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self):
        try:
            product = Product.objects.get(id=self.id)
            if product.image.path!=self.image.path:
                os.remove(product.image.path)
            return super().save()
        except:
            super().save()

    def delete(self, using = None, keep_parents = False) :
        os.remove(self.image.path)
        return super().delete(using, keep_parents)

       