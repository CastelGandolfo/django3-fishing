from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


# Create your views here.
def home(request):
    return render(request, 'fishing/home.html')


def contact(request):
    return render(request, 'fishing/contact.html')

def info(request):
    return render(request, 'fishing/info.html')


    

def products(request):

    products = Product.objects.all()

    return render(request, 'fishing/products.html', {"products": products})


def product(request, product_pk):

    product = get_object_or_404(Product, pk=product_pk)

    if product.photo:
        return render(request, 'fishing/product_photo.html', {"product": product})
    else:
        return render(request, 'fishing/product.html', {"product": product})


