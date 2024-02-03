from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about_us.html")
