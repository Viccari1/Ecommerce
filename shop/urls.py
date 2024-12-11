from .views import index, produto
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('produto/<id>', produto, name='produto'),
]
