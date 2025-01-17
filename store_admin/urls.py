from .views import add_product, create_store, my_store, edit_product
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('minha_loja', my_store, name='my_store'),
    path('criar_loja', create_store, name='create_store'),
    path('add_produto', add_product, name='add_product'),
    path('edit_produto/<int:id>', edit_product, name='edit_product'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
