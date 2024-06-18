from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from cart.models import Cart
from products.models import Product
from django.http import JsonResponse


def add_to_cart(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        response = JsonResponse({'product name': product.name})
        return response