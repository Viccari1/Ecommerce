from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User
from rolepermissions.roles import assign_role
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

# Create your views here.
def redirect_if_logged_in(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return Http404()  # Redirecione para a página inicial ou outra página
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

@redirect_if_logged_in
def register(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.full_clean()
            print(form.cleaned_data.get('role'))
            form.role = form.cleaned_data.get('role')
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role')
            user.save()
            assign_role(user, form.cleaned_data.get('role'))
            authenticated_user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            if user.role == 'vendedor':
                return redirect('create_store')
            return redirect('index')  # Redirecione para a página inicial ou outra página
        
    context = {'form': form}
    return render(request, 'users/criar_usuario.html', context)

def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirecione para a página inicial ou outra página
            form.add_error(None, "Email ou senha incorretos.")

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirecione para a página inicial ou outra página