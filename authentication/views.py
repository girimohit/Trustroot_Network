from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
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


def register_user(request):
    if request.method == "POST":
        user_type = request.POST.get("userType")
        base_form = SignUpForm(request.POST)
        if user_type == "grassroot":
            form = GrassrootProfileForm(request.POST)
        elif user_type == "community":
            form = CommunityUserProfileForm(request.POST)
        elif user_type == "donor":
            form = DonorProfileForm(request.POST)
        else:
            return HttpResponse("Please Select Correct USER type!")

        if base_form.is_valid() and form.is_valid():
            user = base_form.save(commit=False)
            user.full_name = base_form.cleaned_data.get("fullName")
            user.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            # Automatic Login
            login(request=request, user=user)
            return redirect("base:homePage")
        else:
            return HttpResponse("Error Occurred!")
    else:
        context = {
            "registrationForm": SignUpForm(),
            # "loginForm": CustomAuthenticationForm(),
            # "grassroot": GrassrootProfileForm(),
            # "donor": DonorProfileForm(),
            # "community": CommunityUserProfileForm(),
        }
        return render(request, "index.html", context=context)


# def register_user(request):
#     if request.method == "POST":
#         base_form = SignUpForm()
#         user_type = request.POST.get("userType")
#         if user_type == "grassroot":
#             form = GrassrootProfileForm()
#         elif user_type == "donor":
#             form = DonorProfileForm()
#         elif user_type == "community":
#             form = CommunityUserProfileForm()
#         else:
#             return HttpResponse("Please Select Correct USER type!")
#         print(form)
#         if form.is_valid() and base_form.is_valid():
#             # user = form.save(commit=False)
#             # # user.set_password(form.cleaned_data["password1"])
#             # user.save()
#         # if base_form.is_valid() and form.is_valid():
#             # user = base_form.save(commit=False)
#             # user.full_name = base_form.cleaned_data.get("fullName")
#             # user.save()
#             # profile = form.save(commit=False)
#             # profile.user = user
#             # profile.save()
#             # # Automatic Login
#             # login(request=request, user=user)
#             # return redirect("base:aboutPage")
#             return HttpResponse("Forms are Valid")
#         else:
#             # return redirect("base:homePage")
#             return HttpResponse("Error Occured!")
#     else:
#         context = {
#             "registrationForm": SignUpForm(),
#             "loginForm": CustomAuthenticationForm(),
#             "grassroot": GrassrootProfileForm(),
#             "donor": DonorProfileForm(),
#             "community": CommunityUserProfileForm(),
#         }
#         return render(request, "index.html", context=context)


# def register_user(request):
#     if request.method == "POST":
#         user_type = request.POST.get("userType")
#         if user_type == "grassroot":
#             form = GrassrootUserCreationForm()
#         elif user_type == "donor":
#             form = DonorCreationForm()
#         elif user_type == "community":
#             form = CommunityUserCreationForm()
#         else:
#             return HttpResponse(
#                 "Invalid User. You're not authenticated to view this page"
#             )
#         if form.is_valid():
#             # form.save()
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password1"])
#             user.save()
#             # automatic login
#             login(request, user)
#             return redirect("base:homePage")
#     else:
#         context = {
#             "registrationForm": CustomUserCreationForm(),
#             "loginForm": CustomAuthenticationForm(),
#             "grassroot": GrassrootUserCreationForm(),
#             "donor": DonorCreationForm(),
#             "community": CommunityUserCreationForm(),
#         }
#     return render(request, "index.html", context)


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


def logout_user(request):
    logout(request)
    return redirect("base:homePage")


# # def register_user(request):
# #     if request.method == "POST":
# #         user_type = request.POST.get("userType")
# #         print("USER TYPE : ", user_type)
# #         if user_type == "grassroot":
# #             form = GrassrootUserCreationForm(request.POST)
# #         elif user_type == "donor":
# #             form = DonorCreationForm(request.POST)
# #         elif user_type == "community":
# #             form = CommunityUserCreationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)
# #             return redirect("base:homePage")
# #     else:
# #         form = CustomUserCreationForm()
# #     context = {
# #         "registrationForm": CustomUserCreationForm(),
# #         "loginForm": CustomAuthenticationForm(),
# #         "community": CommunityUserCreationForm(),
# #         "donor": DonorCreationForm(),
# #         "grassroot": GrassrootUserCreationForm(),
# #     }
# #     return render(request, "index.html", context=context)
