from django.db.models import Q, F, DecimalField, Prefetch
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, Image


def off_product(request):
    today = timezone.now()

    top_discounted_products = Product.objects.filter(
        Q(discountcode__valid_from__lte=today) &
        Q(discountcode__valid_to__gte=today) &
        (Q(discountcode__discount_type='percent') | Q(discountcode__discount_type='amount'))
    ).annotate(
        discount_type=F('discountcode__discount_type'),
        discount_value=Coalesce(F('discountcode__value'), 0, output_field=DecimalField())
    ).distinct().prefetch_related('images').order_by('-discountcode__value')[:2]

    return render(request, 'off_products.html', {
        'top_discounted_products': top_discounted_products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    image = Image.objects.filter(product=product, title='detail-box').first()
    return render(request, 'product_detail.html', {
        'product': product,
        'image': image,
    })
