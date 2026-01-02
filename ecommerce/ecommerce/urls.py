"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import user_login, user_logout
from products.views import product_list
from orders.views import cart, place_order, my_orders, checkout, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('cart/', cart, name='cart'),
    path('orders/checkout/', checkout, name='checkout'),
    path('orders/remove/<int:order_id>/', remove_from_cart, name='remove_from_cart'),
    path('orders/place/', place_order, name='place_order'),
    path('orders/my-orders/', my_orders, name='my_orders'),
    path('accounts/', include('users.urls')),
]
urlpatterns += [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
