from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from products.models import Product

def place_order(request, product_id):
    product = Product.objects.get(id=product_id)

    Order.objects.create(
        user=request.user,
        product=product,
        quantity=1,
        total_price=product.price
    )

    return redirect('/products/')


@login_required
def cart_view(request):
    cart_items = Order.objects.filter(user=request.user)
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'orders/cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })
@login_required
def remove_from_cart(request, order_id):
        order_item = get_object_or_404(Order, id=order_id, user=request.user)
        order_item.delete()
        return redirect('cart')
@login_required
def cart_view(request):
    cart_items = Order.objects.filter(user=request.user, is_placed=False)
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'orders/cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })
@login_required
def checkout(request):
    cart_items = Order.objects.filter(user=request.user, is_placed=False)

    for item in cart_items:
        item.is_placed = True
        item.save()

    return render(request, 'orders/checkout_success.html')

