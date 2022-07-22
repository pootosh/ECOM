from distutils.log import error
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer

def validate_user_session(id, token):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(id=id)
        if user.session_token == token:
            return True
        return False
    
    except user_model.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Please re-login", "code": "500"})

    if request.method == "POST":
        user_id =id
        transaction_id = request.POST['transaction_id']
        product_names = request.POST['transaction_id']
        total_amount = request.POST['transaction_id']
        total_products = len(product_names.split(","))
        print(total_products)

        user_model = get_user_model()

        try:
            user =  user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return JsonResponse("error", "User does not exist")
        
        order = Order(user = user, total_products=total_products, product_names=product_names,transaction_id=transaction_id, total_amount=total_amount)
        order.save()
        return JsonResponse({"success": True, "error": False, "msg": "Order saved successfully."})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer