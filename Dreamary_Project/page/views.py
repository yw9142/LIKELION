from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def introduce(request):
    return render(request, 'introduce.html')
