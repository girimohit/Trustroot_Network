# myapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from baseapp import views

app_name = "base"
urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("post/", views.post, name="post"),
    path("grassroots/", views.grassroot, name="grassrootPage"),
    path("grassroot-profile/<int:user_id>", views.grassroot_profile, name="grassroot_profile"),
    path("frequently-asked-questions/", views.faq, name="faq_page"),
    path("authforms/", views.authforms, name="authforms")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)