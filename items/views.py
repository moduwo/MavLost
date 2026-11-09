from django.shortcuts import render

# Create your views here.

# display home page
def home(request):
    return render(request, "items/home.html")
