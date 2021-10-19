from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from sales.utils import generate_code


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products')
    price = models.FloatField(help_text='in Kenyan Shillings')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created.strftime('%d/%m/%Y')}"
class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers')

    def __str__(self):
        return self.name
class SalesPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio yet...')
    avatar = models.ImageField(upload_to='avatars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Salesperson {self.user.username}"

class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        
        return super().save(*args, **kwargs)
   
    def __str__(self):
        return f"Sales for the amount of Kshs {self.total_price}"
