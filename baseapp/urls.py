# myapp/urls.py

from django.urls import path
from baseapp import views

app_name = "base"
urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("post/", views.post, name="post")
]

    # url(r'^accounts/login/$', LoginView.as_view(authentication_form=OTPAuthenticationForm)),