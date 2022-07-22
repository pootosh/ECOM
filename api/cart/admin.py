from django.contrib import admin
from .models import Cart
# Register your models here.

class AdminCart(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Cart, AdminCart)