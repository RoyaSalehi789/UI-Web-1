from xml.etree.ElementInclude import include

import products.views
from products import views
from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', products.views.product_detail, name='product-detail'),
]
