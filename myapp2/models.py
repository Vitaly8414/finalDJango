from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(db_index=True)
    phone_number = models.CharField(max_length=15, db_index=True)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True, db_index=True)
