from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import Product
from django.utils import timezone

# Create your models here.

# original 
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail", kwargs={})


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length= 200)
    code = models.IntegerField()

    def __str__(self):
        return self.user.email
    





    """
class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"

    def get_total_product_price(self):
        return self.quantity * self.product.price 
"""


"""
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    checkout = models.ForeignKey('Checkout', on_delete=models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.user.email 

    def get_total_price(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_total_product_price()
        return 
"""

"""
# trial
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    ordered_date = models.DateTimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)
    checkout = models.ForeignKey('Checkout', on_delete=models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_total_price(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_total_product_price()
        return total

    def get_absolute_url(self):
        return reverse("cart:cart_detail", kwargs={})

"""