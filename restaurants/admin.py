from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'restaurant_name', 'price')
