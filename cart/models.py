from django.db import models
from accounts.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def __int__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.name)}
        self.session.modified = True

    class Metta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.PositiveIntegerField()

    class Metta:
        verbose_name = 'cart_item'
        verbose_name_plural = 'carts_item'
