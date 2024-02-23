from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart, Checkout
from home.models import Product
from django.db.models import Sum
from datetime import datetime
from django.views.generic import View
from .forms import CheckoutForm

# Create your views here.

#Original
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=request.user, product=product)
        messages.success(request, "Item added to your cart.")

    return redirect("/cart")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, "Item deleted from your cart.")

            else:
                cart_item.delete()
                messages.success(request, "Item deleted from your cart.")


    return redirect("/cart")


@login_required
def remove_all_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item deleted from your cart.")

    return redirect("/cart")


@login_required
def cart_details(request):
    cart_items = (Cart.objects.filter(user=request.user).select_related('product'))
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    for item in cart_items:
        item.total_item_price = item.quantity * item.product.price

    total_items = cart_items.aggregate(total_items=Sum('quantity'))['total_items'] or 0

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "total_items": total_items,
    }

    return render(request, "cart_details.html", context)


# original
def checkout(request):
    cart_items = (Cart.objects.filter(user=request.user).select_related('product'))
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    for item in cart_items:
        item.total_item_price = item.quantity * item.product.price

    total_items = cart_items.aggregate(total_items=Sum('quantity'))['total_items'] or 0

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "total_items": total_items,
    }

    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        code = request.POST.get('code')
        user = request.user
        checkout_details = Checkout(user=user, phone=phone, address=address, code=code)
        checkout_details.save()
        messages.success(request, "Your order has been placed")

    return render(request, "checkout.html", context)





"""
# trial

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        cart = Cart.objects.get(user=self.request.user, ordered=False)
        context = {
            'form': form,
            'cart': cart
        }
        return render(self.request, 'checkout2.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            cart = Cart.objects.get(user=self.request.user,ordered = False)
            if form.is_valid():
                phone = form.cleaned_data.get('phone')
                address = form.cleaned_data.get('address')
                code = form.cleaned_data.get('code')

                checkout_details = Checkout( user = self.request.user, phone=phone, address=address, code=code)
                checkout_details.save()
                cart.checkout_details = checkout_details
                cart.save()
                messages.success(request, "Your order has been placed")
                
            return redirect('/')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect('/')
"""

"""
#Trial
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_product, created = OrderProduct.objects.get_or_create(product = product, user=request.user, ordered=False)
    cart_qs = Cart.objects.filter(user=request.user, ordered= False)

    if cart_qs.exists():
        cart = cart_qs[0]

        if cart.products.filter(product__product_id=product.product_id).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Item added to your cart.")
    
        else:
            cart.products.add(order_item)
            messages.success(request, "Item added to your cart.")
            return redirect("/cart")

    else:
        ordered_date = timezone.now()
        cart = Cart.objects.create(user=request.user, ordered_date = ordered_date)
        cart.items.add(order_item)
        messages.success(request, "Item added to your cart.")
    return redirect("/cart")
"""