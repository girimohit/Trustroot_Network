from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpRequest, HttpResponse

# from baseapp.forms import CustomUserCreationForm, CustomAuthenticationForm
from authentication.forms import (
    SignUpForm,
    CustomAuthenticationForm,
    GrassrootProfileForm,
    DonorProfileForm,
    CommunityUserProfileForm,
)


# Create your views here.
def home(request):
    username = request.user.username
    context = {
        "registrationForm": SignUpForm(),
        "loginForm": CustomAuthenticationForm(),
        "username": username,
        "grassroot": GrassrootProfileForm(),
        "donor": DonorProfileForm(),
        "community": CommunityUserProfileForm(),
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about_us.html")


def post(request):
    return render(request, "post.html")


def grassroot(request):
    return render(request, "grassroot.html")
