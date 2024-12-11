from django import forms
from .models import Produto, ImagemProduto, Loja
from django.forms import ClearableFileInput

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'imagemprincipal']
        labels = {
            'nome': 'Nome do produto',
            'descricao': 'Descrição',
            'preco': 'Preço',
            'estoque': 'Estoque',
            'imagemprincipal': 'Imagem principal',
        }

class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']
    imagem = forms.ImageField(widget=ClearableFileInput(), required=False)

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone', 'descricao', 'logo']
        labels = {
            'nome': 'Nome da loja',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'descricao': 'Descrição',
            'logo': 'Logo',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': True}),
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }
    logo = forms.ImageField(widget=ClearableFileInput(), required=False)