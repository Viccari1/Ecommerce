from .views import add_product
from django.urls import path

urlpatterns = [
    path('add_produto', add_product, name='add_product'),
]