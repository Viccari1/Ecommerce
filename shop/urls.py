from .views import index, product, store, add_cart, cart
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('produto/<id>', product, name='product'),
    path('loja/<id>', store, name='store'),
    path('carrinho/', cart, name='cart'),
    path('carrinho/adicionar/<id>', add_cart, name='add_cart'),
]
