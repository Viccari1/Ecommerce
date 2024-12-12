from django.shortcuts import render, redirect
from .forms import ProdutoForm, ImagemProdutoForm, LojaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from users.models import User
from .models import Produto
from store_admin.models import Loja
from rolepermissions.checkers import has_permission, has_role

# Create your views here.
@login_required
def minha_loja(request):
    if not has_role(request.user, 'vendedor') or request.user.is_superuser:
        return HttpResponseForbidden()
    
    if not Loja.objects.filter(dono=request.user).exists():
        return redirect('create_store')
    loja = Loja.objects.get(dono=request.user)
    produtos = Produto.objects.filter(loja=loja)
    context = {'loja': loja, 'produtos': produtos}
    return render(request, 'loja/minha_loja.html', context)

@login_required
def create_store(request):
    if not has_role(request.user, 'vendedor') or request.user.is_superuser:
        return HttpResponseForbidden()
    
    if Loja.objects.filter(dono=request.user).exists():
        return HttpResponseForbidden(['Erro 403: Forbidden!', "<br>", 'Você não tem permissão para ver esta página, pois você só pode ter uma loja, e você já tem uma.', "<br>", 'Se isso parecer estranho, contate um administrador.'])

    if request.method != 'POST':
        form = LojaForm()
    else:
        form = LojaForm(request.POST, request.FILES)
        
        if form.is_valid():
            loja = form.save(commit=False)
            loja.dono = request.user
            loja.email = request.user.email
            loja.save()

            return redirect('index')
    
    context = {'form': form}
    return render(request, 'loja/create_store.html', context)

@login_required
def add_product(request):
    if request.method != 'POST':
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.loja = Loja.objects.get(dono=request.user)
            produto.save()
            
            return redirect('minha_loja')
    
    context = {'form': form}
    return render(request, 'loja/add_product.html', context)

def edit_product(request, id):
    pass