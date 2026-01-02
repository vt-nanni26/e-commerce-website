from django.urls import path
from .views import product_list, add_to_cart, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('<int:id>/', product_detail, name='product_detail'),

]
