from .views import index, product
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('produto/<id>', product, name='product'),
]
