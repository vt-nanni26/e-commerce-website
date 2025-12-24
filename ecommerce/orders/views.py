from django.shortcuts import redirect
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
