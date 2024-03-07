from django.contrib import admin
from authentication.models import (
    CustomUser,
    GrassrootProfile,
    DonorProfile,
    CommunityUserProfile,
)

# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(GrassrootProfile)
admin.site.register(DonorProfile)
admin.site.register(CommunityUserProfile)