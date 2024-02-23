from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import Product
from math import ceil
from .forms import ContactForm
from django.views.generic.edit import FormView

from django.views.generic import DetailView, ListView, View

# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "index2.html"
    context_object_name = 'product'

# def home(request):
#     all_products = Product.objects.all()
#     n = len(all_products)
#     items_per_row = 3
#     nSlides = n // items_per_row + ceil((n / items_per_row) - (n // items_per_row))
#     allProds = [all_products[i:i + items_per_row] for i in range(0, n, items_per_row)]
#     params = {'allProds': allProds, 'nSlides': range(1, nSlides + 1), 'items_per_row': items_per_row}

#     return render(request, 'index.html', params)


class ProductView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs.get('product_id')
        return get_object_or_404(Product, id=product_id)


class MyFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent")
        return super().form_valid(form) 


