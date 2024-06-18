from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main_module.urls')),
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('cart.urls'))
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
