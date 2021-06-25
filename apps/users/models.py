from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class Users(AbstractUser):
    class Meta:
        db_table = "users"

    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class SystemInformation(models.Model):
    class Meta:
        db_table="sys_info"

    store_name = models.CharField(max_length=255, null=False, blank=False)
    store_phone = models.CharField(max_length=255, null=False, blank=False)
    store_email = models.EmailField(max_length=255)
    store_address = models.CharField(max_length=1024, null=False, blank=False)
    