from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.cart, name="cart"),
    path(r'^add/(<int:product_id>)', views.cart_add, name='cart_add'),
    path(r'^remove/(<int:product_id>)', views.cart_remove, name='cart_remove'),  
]