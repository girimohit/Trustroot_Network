from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# ---------------------------- Custom SignUp Form ---------------------------- #
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Cofirm the Password"})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


# ---------------------------- Custom Login Forms ---------------------------- #
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    class Meta:
        fields = ("username", "password")


# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(
#         label="Username", max_length=50, help_text="Don't use special characters"
#     )
#     password1 = forms.CharField(label="Password")
#     password2 = forms.CharField(label="Confirm Password")
#     # password2 = forms.CharField(label="<PASSWORD>", widget=forms.PasswordInput

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")
#         widgets = {
#             "username": forms.TextInput(attrs={"placeholder": "Username"}),
#             "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
#             "password2": forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
#         }
#         # widgets = {
#         #     "password1": forms.PasswordInput,
#         #     "password2": forms.PasswordInput,
#         # }
#         # labels = {
#         #     "username": "Username",
#         #     "password1": "Password",
#         #     "password2": "<PASSWORD>",
#         # }
#         # help_texts = {
#         #     "username": "Letters, digits and @/./+/-/_ only.",
#         #     "password1": "<PASSWORD>.",
#         #     "password2": "<PASSWORD>.",
#         # }
#         # error_messages = {
#         #     "username": {"unique": "A user with that username already exists."},
#         #     "password1": {
#         #         "min_length": "Your password must be at least 5 characters long."
#         #     },
#         #     "password2": {
#         #         "min_length": "Your password must be at least 5 characters long."
#         #     },
#         # }
