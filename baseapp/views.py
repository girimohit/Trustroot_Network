from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(request):
    form = UserCreationForm()
    # context = {'signform' : form}
    return render(request, 'index.html')



def about(request):
    return render(request, "about_us.html")
