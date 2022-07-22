from django.urls import path, include
from rest_framework.authtoken import views
from .views import Home
urlpatterns = [
    path('', Home, name='api_home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('cart/', include('api.cart.urls')),
    path(r'api-token-auth/', views.obtain_auth_token, name='token'),
]