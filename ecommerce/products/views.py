from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from orders.models import Order
def product_list(request):
    # return HttpResponse("product list page working")
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def add_to_cart(request, product_id):
    cart=request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Order.objects.create(
        user=request.user,
        product=product,
        quantity=1,
        total_price=product.price
    )

    return redirect('product_list')