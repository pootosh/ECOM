from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse
import re

import random
# Create your views here.

def generate_session_token(length=10):
    lst = [chr(i) for i in range(97,123)] + [str(i) for i in range(10)]
    token = "".join(random.SystemRandom().choice(lst) for _ in range(10))
    return token

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Invalid request method'})
    
    username = request.POST.get('email')
    password = request.POST.get('password')
    email_verification_regex = "\w+@[a-z]+\.[a-z]{2,3}"

    if not re.match(email_verification_regex, username):
        return JsonResponse({'error': 'Invalid email id'})
    
    if len(password) < 3:
        return JsonResponse({'error': 'Password must be at least 3 characters'})
    
    user_model = get_user_model()

    try:
        user = user_model.objects.get(email=username)
        print('user',user.session_token)
        if user.check_password(password):
            usr_dict = user_model.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'Previous session exist'})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            print(request.user)
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        
        else:
            return JsonResponse({'error': 'Incorrect Password'})

    except user_model.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'})


def signout(request, id):
    logout(request)
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk = id)
        user.session_token = "0"
        user.save()
    except user_model.DoesNotExist:
        return JsonResponse({'error': 'Invalid id'})
    
    return JsonResponse({'success': 'Logout Success'})

class UserViewSet(viewsets.ModelViewSet):


    permission_classes_by_action = {'create': [AllowAny,]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes]
    