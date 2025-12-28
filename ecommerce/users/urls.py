from django.urls import path
from . import views
from . views import signup

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', signup, name='signup'),

]
