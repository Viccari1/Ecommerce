from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def redirect_if_logged_in(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirecione para a página inicial ou outra página
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

def redirect_to_login(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirecione para a página de login
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func