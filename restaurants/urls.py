# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.restaurant_menu, name='restaurant_menu'),
    path('menu/<path:url>/', views.restaurant_menu, name='menu_url'),
]
