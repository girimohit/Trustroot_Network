from django.urls import path
from donors import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Define more URL patterns as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
