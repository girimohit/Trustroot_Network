# myapp/urls.py

from django.urls import path
from baseapp import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
]
