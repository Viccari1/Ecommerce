from django.shortcuts import render
from store_admin.models import Produto
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    # carrinho = request.session.get('carrinho', {})
    # request.session.set()
    pass
    context = {'produtos': Produto.objects.all()}
    return render(request, 'index.html', context)

def produto(request, id):
    try:
        produto = Produto.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist('Produto não encontrado!')
    context = {'produto': produto}
    return render(request, 'produto.html', context)