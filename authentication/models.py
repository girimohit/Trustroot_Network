from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=100)


class GrassrootProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)


class DonorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField()
    paymentMethod = models.CharField(max_length=30)
    firmName = models.CharField(max_length=100)


class CommunityUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
