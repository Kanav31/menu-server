# restaurants/models.py
from django.db import models

class MenuItem(models.Model):
    restaurant_name = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} - {self.price}"
