from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from authentication.forms import (
    SignUpForm,
    CustomAuthenticationForm,
    GrassrootProfileForm,
    DonorProfileForm,
    CommunityUserProfileForm,
)
from authentication.models import (
    CustomUser,
    GrassrootProfile,
    DonorProfile,
    CommunityUserProfile,
)


# ------------------------- Register/Signup User View ------------------------ #
def register_user(request):
    if request.method == "POST":
        base_form = SignUpForm(request.POST)
        type = request.POST.get("usertype")
        profile_icon = request.POST.get("profile_icon")
        print(type)
        print(profile_icon)
        if type == "grassroot":
            if profile_icon:
                print("Got the profile")
                form = GrassrootProfileForm(request.POST, request.FILES)
            form = GrassrootProfileForm(request.POST, request.FILES)
        elif type == "community":
            form = CommunityUserProfileForm(request.POST)
        elif type == "donor":
            form = DonorProfileForm(request.POST)
        else:
            return JsonResponse({"error": "Invalid user type"}, safe=False)
        # print(form)

        if base_form.is_valid() and form.is_valid():
            print("Form is valid")
            base_user = base_form.save(commit=False)
            base_user.user_type = type
            base_user.save()
            form.instance.user = base_user
            # form.instance.profile_icon = profile_icon
            print("profile form is going to be saved")
            form.save()
            # Automatic login
            login(request, base_user)
            return redirect("base:homePage")

        elif form:
            print(base_form.is_valid())
            print(form.is_valid())
            print("Form is there but not valid maybe")
            field_html = ""
            base_fields = base_form.visible_fields()
            for j in base_fields:
                field_html += str(j)
            # Render only the form fields
            fields = form.visible_fields()
            for i in fields:
                field_html += str(i)

            return JsonResponse({"additional_fields": field_html})
        else:
            return JsonResponse({"error": "Invalid Request"}, safe=False)

    else:
        # Render the initial form template
        print("Not a POST request")
        return render(request, "auth/signup.html")


# ------------------------------ Login User View ----------------------------- #
def login_user(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("base:homePage")
    else:
        form = CustomAuthenticationForm()
    return render(request, "index.html", {"loginForm": form})


# ----------------------------- Logout User View ----------------------------- #
def logout_user(request):
    logout(request)
    return redirect("base:homePage")
