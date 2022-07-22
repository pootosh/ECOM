from django.urls import path, include
from . import views

urlpatterns = [
    path('generate_token/<str:id>/<str:token>', views.generate_token),
    path('process_payment/<str:id>/<str:token>', views.process_payment),

]