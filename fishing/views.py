from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, About, Contact, HomeInfo


# Create your views here.
def home(request):

    homeinfo = HomeInfo.objects.all()
    return render(request, 'fishing/home.html', {"homeinfo": homeinfo[0]})


def contact(request):

    contact = Contact.objects.all()

    return render(request, 'fishing/contact.html', {"contact": contact[0]})

def info(request):
    about = About.objects.all()

    return render(request, 'fishing/info.html', {"about": about[0]})


    

def products(request):

    products = Product.objects.all()

    return render(request, 'fishing/products.html', {"products": products})


def product(request, product_pk):

    product = get_object_or_404(Product, pk=product_pk)

    if product.photo:
        return render(request, 'fishing/product_photo.html', {"product": product})
    else:
        return render(request, 'fishing/product.html', {"product": product})


