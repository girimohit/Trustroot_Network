from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.conf import settings

# from baseapp.forms import CustomUserCreationForm, CustomAuthenticationForm
from authentication.forms import (
    SignUpForm,
    CustomAuthenticationForm,
    GrassrootProfileForm,
    DonorProfileForm,
    CommunityUserProfileForm,
)
from authentication.models import GrassrootProfile, Follow


# Create your views here.
def home(request):
    username = request.user.username
    mediafolder = settings.MEDIA_ROOT
    mediaurl = settings.MEDIA_URL
    print(mediafolder)
    print("URL : ", mediaurl)
    context = {
        "registrationForm": SignUpForm(),
        "loginForm": CustomAuthenticationForm(),
        # "username": username,
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
    return render(request, "grassroot/grassroots_page.html", context=context)


def grassroot_profile(request, user_id):
    id_from_url = user_id
    print(id_from_url)
    
    grassroot_profile = get_object_or_404(GrassrootProfile, user_id=user_id)
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=grassroot_profile).exists()
    else:
        is_following = ""
    context = {
        "grassroot_profile": grassroot_profile,
        "profile_id": id_from_url,
        "is_following": is_following,
    }
    return render(request, "grassroot/grassroot_profile.html", context)


def faq(request):
    return render(request, "faq.html")


def authforms(request):
    context = {
        "registrationForm": SignUpForm(),
        "loginForm": CustomAuthenticationForm(),
    }
    return render(request, "auth/signup.html", context)
