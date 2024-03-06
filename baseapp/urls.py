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
    path("grassroot-profile/", views.grassroot_profile, name="grassroot_profile"),
    path("frequently-asked-questions/", views.faq, name="faq_page"),
    path("save_grassroot/", views.save_grassroot, name="save_grassroot")
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url(r'^accounts/login/$', LoginView.as_view(authentication_form=OTPAuthenticationForm)),
