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
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagemprincipal': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']
        widgets = {
            'imagem': ClearableFileInput(attrs={'class': 'form-control'}),
        }

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
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'logo': ClearableFileInput(attrs={'class': 'form-control'}),
        }
    logo = forms.ImageField(widget=ClearableFileInput(), required=False)
