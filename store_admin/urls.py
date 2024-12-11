from .views import add_product, create_store, minha_loja
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('minha_loja', minha_loja, name='minha_loja'),
    path('criar_loja', create_store, name='create_store'),
    path('add_produto', add_product, name='add_product'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
