from django import forms
from .models import Produto, ImagemProduto, Loja
from django.forms import ClearableFileInput

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'loja', 'estoque', 'vendidos', 'imagemprincipal', 'imagens', 'avaliacao']
    
    imagens = forms.ImageField(widget=ClearableFileInput(), required=False)

class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['nome', 'dono']