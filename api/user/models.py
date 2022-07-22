from ssl import create_default_context
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Gender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        NONE = "None"

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.NONE)

    session_token = models.CharField(max_length=10, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)