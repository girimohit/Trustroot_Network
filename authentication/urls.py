# authentication/urls.py
from django.urls import path
from authentication.views import login_user, register_user, logout_user
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

