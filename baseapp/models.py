from django.db import models
from django.core.validators import validate_email


# class Grassroots(models.Model):
#     profile_icon = models.ImageField(upload_to="grassroot_profile_icons/")
#     name = models.CharField(max_length=100)
#     focus_area = models.TextField()
#     email = models.EmailField(validators=[validate_email])
#     contact_number = models.CharField(max_length=20, null=True, blank=True)

#     def __str__(self):
#         return self.name
