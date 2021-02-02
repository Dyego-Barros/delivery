from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.conf import settings

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})  
        set_string = str(item['quantity'])
        for letra in item:
            letra = set_string
            return render(request, 'cart/detail.html', {'cart': cart})
    return render(request, 'cart/detail.html', {'cart': cart})

def  cart_update(request, product_id):
     cart = Cart(request)
     product = get_object_or_404(Product, id=product_id)
     form = CartAddProductForm(request.POST or None, instance=product )
     if  form.is_valid():            
            cart.add(product=product,quantity=['quantity'],update_quantity=['update'])
     return render(request, 'cart/detail.html')


def cart_remove_clear(request):
    cart = Cart(request)
    cart.clear() 
    return redirect('cart:cart_detail')




