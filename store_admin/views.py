from django.shortcuts import render
from .forms import ProdutoForm, ImagemProdutoForm, LojaForm

# Create your views here.
def add_product(request):
    if request.method != 'POST':
        form = ProdutoForm()
    else:
        produto_form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'shop/index.html')
    
    context = {'form': form}
    return render(request, 'store/add_product.html', context)
