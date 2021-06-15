from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, "products/listado.html", {"products": products})