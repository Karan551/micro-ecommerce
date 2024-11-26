from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProductForm, ProductUpdateForm
from .models import Product
# Create your views here.


def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            if request.user.is_authenticated:
                product.user = request.user
                product.save()
                return redirect("/products/create/")
            else:
                form.add_error(None, "Please Login to add new product.")
                return render(request, "products/create.html", {"form": form})

    else:
        return render(request, "products/create.html", {"form": form})


def product_list_view(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail_view(request, product_slug=None):
    product = get_object_or_404(Product, product_slug=product_slug)
    
    is_owner = False
    if request.user.is_authenticated:
        is_owner = product.user == request.user
        if is_owner:
            form = ProductUpdateForm(
                request.POST or None, request.FILES or None, instance=product)
            
            if form.is_valid():

                form.save()

            return render(request, "products/product_detail.html", {"product": product, "form": form})

    return render(request, "products/product_detail.html", {"product": product})
