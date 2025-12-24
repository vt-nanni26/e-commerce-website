from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
def product_list(request):
    # return HttpResponse("product list page working")
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def add_to_cart(request, product_id):
    cart=request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')