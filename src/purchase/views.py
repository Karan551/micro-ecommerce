from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from products.models import Product
from purchase.models import Purchase

# Create your views here.


def purchase_start_view(request):
    if not request.method == "POST":
        return HttpResponseBadRequest()

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()

    product_slug = request.POST.get("handle")
    product = Product.objects.get(product_slug=product_slug)

    obj = Purchase.objects.create(user=request.user, product=product)
    print("this is session", request.session)

    request.session["purchase_id"] = obj.id

    # for i in request.session.items():
    #     print("this is session:", i)
    print("after buy this is session", request.session)
    print("this is handle::", product_slug)
    print("this is product::", product)
    # print("this is purchase id::", obj.id)

    return HttpResponseRedirect("/purchase/stop/")


def purchase_stop_view(request):

    return HttpResponse(f"Stopped")


def purchase_success_view(request):
    purchase_id = request.session.get("purchase_id")
    name = None
    if purchase_id:
        obj = Purchase.objects.get(id=purchase_id)
        name = obj.product
        obj.completed = True
        obj.save()

    return HttpResponse(f"Thanks for buying {name} --- {purchase_id}")
