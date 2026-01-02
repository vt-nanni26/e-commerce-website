from django.urls import path
from .views import cart, place_order, my_orders, checkout, remove_from_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('remove/<int:order_id>/', remove_from_cart, name='remove_from_cart'),
    path('place/', place_order, name='place_order'),
    path('my-orders/', my_orders, name='my_orders'),
]
