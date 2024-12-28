from django.shortcuts import render
from store_admin.models import Product
from django.core.exceptions import ObjectDoesNotExist

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