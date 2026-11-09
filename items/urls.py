from django.urls import path
from . import views

# map URLs to views
urlpatterns = [
    path('', views.home, name='home'),
    path('items/new/', views.create_item, name='create_item'),
    path('items/', views.item_list, name='item_list'),
]