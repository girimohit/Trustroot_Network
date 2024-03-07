from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser


USERTYPE_CHOICES = [
    ("grassroot", "Grassroot"),
    ("donor", "Donor"),
    ("community", "Community"),
]


class CustomUser(AbstractUser):
    # fullName = models.CharField(max_length=100)
    user_type = models.CharField(max_length=25, choices=USERTYPE_CHOICES)


class GrassrootProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_icon = models.ImageField(upload_to="grassroot_profile_icons/")
    org_name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    focus_area = models.TextField(default="None", null=True, blank=True)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    sdg = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.org_name


class DonorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
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


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name = 'following', on_delete=models.CASCADE)
    following = models.ForeignKey('GrassrootProfile', related_name = 'followers' ,on_delete=models.CASCADE)
    follower_created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.user.username}"