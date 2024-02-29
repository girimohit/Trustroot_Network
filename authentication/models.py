from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=100)


class GrassrootProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_icon = models.ImageField(upload_to="grassroot_profile_icons/")
    org_name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    focus_area = models.TextField(default="None", null=True, blank=True)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    sdg = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.org_name


class DonorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField()
    paymentMethod = models.CharField(max_length=30)
    firmName = models.CharField(max_length=100)

    def __str__(self):
        return self.user.fullName


class CommunityUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.fullName
