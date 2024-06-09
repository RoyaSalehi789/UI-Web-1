from django.contrib import admin
from django.urls import path, include
from main_module import views

urlpatterns = [
    path('', include('main_module.urls')),
    path('admin/', admin.site.urls),]
