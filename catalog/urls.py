from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import product_list, product_detail
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
