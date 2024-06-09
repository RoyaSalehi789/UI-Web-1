from django.db import models
from products.models import Product, Category


class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10, choices=[('percent', 'Percent'), ('amount', 'Amount')])
    value = models.DecimalField(max_digits=10, decimal_places=2)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    applicable_to_products = models.ManyToManyField(Product, blank=True)
    applicable_to_categories = models.ManyToManyField(Category, blank=True)
