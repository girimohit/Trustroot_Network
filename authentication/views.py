from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or home page
            return redirect('homePage')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})


def login_user(request):
    pass