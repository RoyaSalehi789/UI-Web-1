from xml.etree.ElementInclude import include
from products.views import product_detail
from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('signup/', views.register, name='sign_up'),
    path('activate-account/<email_active_code>', views.activate_account, name='activate_account'),
]
