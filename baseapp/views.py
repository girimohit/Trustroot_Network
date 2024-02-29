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
from authentication.models import GrassrootProfile


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
    grassroots = GrassrootProfile.objects.all()

    location = request.GET.get("location")
    focus_area = request.GET.get("focus_area")
    sdg = request.GET.get("sdg")
    # profiles = GrassrootProfile.objects.get(id=1)
    if location:
        grassroots = grassroots.filter(location=location)
    if focus_area:
        grassroots = grassroots.filter(focus_area=focus_area)
    if sdg:
        grassroots = grassroots.filter(sdg=sdg)

    context = {"grassroots": grassroots}
    return render(request, "grassroot.html", context=context)


def grassroot_profile(request):
    return render(request, "grassroot_profile.html")


def faq(request):
    return render(request, "faq.html")


def save_grassroot(request):
    pass
