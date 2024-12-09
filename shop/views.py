from django.shortcuts import render
from store_admin.models import Produto

# Create your views here.
def index(request):
    # carrinho = request.session.get('carrinho', {})
    # request.session.set()
    pass
    context = {'produtos': Produto.objects.all()}
    return render(request, 'index.html', context)