from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_executor = models.BooleanField(default=False)


class CustomerProfile(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=200)
    experience = models.TextField()

    def __str__(self):
        return f'Profile of Customer {self.customer.username}'


class ExecutorProfile(models.Model):
    executor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=200)
    experience = models.TextField()

    def __str__(self):
        return f'Profile of Executor {self.executor.username}'
