from django.shortcuts import render, redirect
from store_admin.models import Product, Store
from django.core.exceptions import ObjectDoesNotExist
from core.utils import redirect_to_login

# Create your views here.
def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'shop/index.html', context)

def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist('Produto não encontrado!')
    context = {'product': product}
    return render(request, 'shop/product.html', context)

def store(request, id):
    try:
        store = Store.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist('Loja não encontrada!')
    
    context = {'store': store, 'products': Product.objects.filter(store=store)}
    if store.owner != request.user:
        return render(request, 'shop/store.html', context)
    return redirect('my_store')

@redirect_to_login
def cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum([product.price for product in products])
    context = {'products': products, 'total': total}
    return render(request, 'shop/cart.html', context)

@redirect_to_login
def add_cart(request, id):
    product = Product.objects.get(id=id)
    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart
    return redirect('index')