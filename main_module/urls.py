from xml.etree.ElementInclude import include

from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('signup/', views.register, name='sign_up')
]
