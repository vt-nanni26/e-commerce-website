from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def place_order(request):
    # Cart items = orders not yet placed (simple logic)
    orders = Order.objects.filter(user=request.user, is_placed=False)

    if orders.exists():
        for order in orders:
            order.is_placed = True
            order.save()
        return redirect('my_orders')
    return redirect('cart')

@login_required
def remove_from_cart(request, order_id):
        order_item = get_object_or_404(Order, id=order_id, user=request.user)
        order_item.delete()
        return redirect('cart')
@login_required
def cart(request):
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

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_placed=True)
    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })

