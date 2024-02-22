# authentication/urls.py
from django.urls import path
from authentication.views import register_user, login_user

app_name = "accounts"
urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
]
