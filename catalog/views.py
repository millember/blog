from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    product = (Product.objects.all())
    context = {"product": product}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product_details = get_object_or_404(Product, pk=pk)
    context = {"product_details": product_details}
    return render(request, "product_detail.html", context)


