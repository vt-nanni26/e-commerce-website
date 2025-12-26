from django.urls import path
from .views import cart_view, remove_from_cart, checkout

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('cart/remove/<int:order_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]
