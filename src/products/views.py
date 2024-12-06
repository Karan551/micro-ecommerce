from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest
from .forms import ProductForm, ProductUpdateForm, ProductAttachmentInlineFormSet
from .models import Product, ProductAttachMent
import mimetypes


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
    product = get_object_or_404(
        Product,
        product_slug=product_slug)

    attachments = ProductAttachMent.objects.filter(product=product)

    is_owner = False

    if request.user.is_authenticated:
        # HERE may be we can change (alomost done)
        is_owner = product.user == request.user
        if is_owner:
            return render(request,
                          "products/product_detail.html",
                          {
                              "product": product,
                              "is_owner": is_owner,
                              "attachments": attachments,
                          })

    return render(request, "products/product_detail.html", {"product": product})


def product_manage_detail_view(request, product_slug=None):
    # HERE  observe this view again
    product = get_object_or_404(Product, product_slug=product_slug)

    context = {"product": product}
    attachments = ProductAttachMent.objects.filter(product=product)
    is_manager = False

    if request.user.is_authenticated:
        is_manager = product.user == request.user

    if not is_manager:
        return HttpResponseBadRequest()

    form = ProductUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=product)

    formset = ProductAttachmentInlineFormSet(
        request.POST or None,
        request.FILES or None,
        queryset=attachments

    )
       
    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save(commit=False)
     

        for _form in formset:
            attachment_obj = _form.save(commit=False)
            attachment_obj.product = product
            attachment_obj.save()

        return redirect(product.get_manage_url())

    context["form"] = form
    context["formset"] = formset

    return render(request, "products/manager.html", context)


def product_attachment_download_view(request, product_slug=None, pk=None):
    # if image is free then it is visible to all user
    # if user is authenticated then download image free not free don't care

    # HERE we use field lookup
    attachment = get_object_or_404(
        ProductAttachMent, pk=pk, product__product_slug=product_slug)

    print("this is attachment::", attachment.display_name)
    can_download = attachment.is_free or False
    if request.user.is_authenticated:
        can_download = True

    if not can_download:
        return HttpResponseBadRequest()

    file = attachment.file.open("rb")
    filename = attachment.file.name

    content_type, _ = mimetypes.guess_type(filename)
    response = FileResponse(file)
    response["Content-Type"] = content_type or "application/octet-stream"

    # if we want to download the image then
    # HERE we will change the value of inline -> attachment , to download the image
    response["Content-Disposition"] = f"inline;filename={filename}"
    return response
