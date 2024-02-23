from django.contrib import admin
from django.urls import path
from cart import views
from . import views

app_name = 'home'

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.HomeView.as_view(), name = 'home'),
    path('contact', views.MyFormView.as_view(), name = 'contact'),


    path('product/<int:product_id>/', views.ProductView.as_view(), name='productview'),

    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]
