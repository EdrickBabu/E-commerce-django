from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>", views.remove_from_cart, name="remove_from_cart"),
    path("remove_all/<int:cart_item_id>", views.remove_all_from_cart, name="remove_all_from_cart"),
    path("cart", views.cart_details, name="cart_detail"),
    path('checkout', views.checkout, name = 'checkout'),
    
    # path('checkout', views.CheckoutView.as_view(), name = 'checkout'),
]