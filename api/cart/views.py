from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

@csrf_exempt
def UpdateCart(request,  id, token):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=id)
        cart_of_user = Cart.objects.get(user = user)
        print(user)
        print(cart_of_user)
        return JsonResponse({'status': 'success'})
    except user_model.DoesNotExist:
        return JsonResponse({'error': 'user does not exist'})

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
