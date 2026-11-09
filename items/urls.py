from django.urls import path
from . import views

# map URLs to views
urlpatterns = [
    path("", views.home, name="home")
]