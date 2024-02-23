from django.db import models
from django.shortcuts import reverse



# class Category(models.Model):
#     name = models.CharField(max_length=100)


# Create your models here.
CATEGORY = (
    ('Cake', 'Cake'),
    ('Ice Cream', 'Ice cream'),
    ('Shake', 'Shake'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(choices=CATEGORY, max_length=10)
    subcategory = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='images')
    id = models.BigAutoField(primary_key=True, serialize=False)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("cart:add_to_cart", kwargs= {"product_id" : self.pk})

    def get_add_to_cart_url(self):
        return reverse("cart:add_to_cart", kwargs= {"product_id": self.pk})

    def get_remove_from_cart_url(self):
        return reverse("cart:remove_from_cart", kwargs= {"product_id": self.pk})

    def get_remove_all_from_cart_url(self):
        return reverse("cart:remove_all_from_cart", kwargs= {"product_id": self.pk})


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    message = models.TextField()

    def __str__(self):
        return self.name
    