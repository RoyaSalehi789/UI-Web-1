from django.db.models import Q, F, DecimalField
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . import models
from .models import Product


def off_product(request):
    today = timezone.now()

    top_discounted_products = Product.objects.filter(
        Q(discountcode__valid_from__lte=today) &
        Q(discountcode__valid_to__gte=today) &
        Q(discountcode__discount_type='percent') |
        Q(discountcode__discount_type='amount')
    ).annotate(
        discount_type=F('discountcode__discount_type'),
        discount_value=Coalesce(F('discountcode__value'), 0, output_field=DecimalField())
    ).distinct().order_by('-discountcode__value')[:2]
    # for product in discounted_products:
    #     print(
    #         f'Product Name: {product.name}, Discount Type: {product.discount_type}, Discount Value: '
    #         f'{product.discount_value}')

    return render(request, 'off_products.html', {
        'top_discounted_products': top_discounted_products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {
        'product': product
    })
