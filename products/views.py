from django.shortcuts import render

# Create your views here.
from products.product_form import Product_form


def create_product(request):
    product_form = Product_form()
    context = {"form": product_form}
    return render(request, "product/create_product_page.html", context)


def product_page(request):
    return render(request, "/product/product_page.html")


def product_detail(request):
    return render(request, "../templates/product/product_detail.html.html")
