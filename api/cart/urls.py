from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.CartViewSet)

urlpatterns = [
    path('updateCart/<str:id>/<str:token>', views.UpdateCart, name='Update Cart'),
    path('', include(router.urls))
]