from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageForm, StoreForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from users.models import User
from .models import Product, Store
from rolepermissions.checkers import has_permission, has_role

# Create your views here.
@login_required
def my_store(request):
    if not has_role(request.user, 'seller') or request.user.is_superuser:
        return HttpResponseForbidden()
    
    if not Store.objects.filter(owner=request.user).exists():
        return redirect('create_store')
    store = Store.objects.get(owner=request.user)
    products = Product.objects.filter(store=store)
    context = {'store': store, 'products': products}
    return render(request, 'store_admin/my_store.html', context)

@login_required
def create_store(request):
    if not has_role(request.user, 'seller') or request.user.is_superuser:
        return HttpResponseForbidden()
    
    if Store.objects.filter(owner=request.user).exists():
        return HttpResponseForbidden(['Erro 403: Forbidden!', "<br>", 'Você não tem permissão para ver esta página, pois você só pode ter uma loja, e você já tem uma.', "<br>", 'Se isso parecer estranho, contate um administrador.'])

    if request.method != 'POST':
        form = StoreForm()
    else:
        form = StoreForm(request.POST, request.FILES)
        
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.email = request.user.email
            store.save()

            return redirect('index')
    
    context = {'form': form}
    return render(request, 'store_admin/create_store.html', context)

@login_required
def add_product(request):
    if request.method != 'POST':
        form = ProductForm()
    else:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = Store.objects.get(owner=request.user)
            product.save()
            
            return redirect('my_store')
    
    context = {'form': form}
    return render(request, 'store_admin/add_product.html', context)

def edit_product(request, id):
    pass
