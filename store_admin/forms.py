from django import forms
from .models import Product, ProductImage, Store
from django.forms import ClearableFileInput

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'main_image']
        labels = {
            'name': 'Nome do produto',
            'description': 'Descrição',
            'price': 'Preço',
            'stock': 'Estoque',
            'main_image': 'Imagem principal',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control'}),
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'phone', 'description', 'logo']
        labels = {
            'name': 'Nome da loja',
            'address': 'Endereço',
            'phone': 'Telefone',
            'description': 'Descrição',
            'logo': 'Logo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'logo': ClearableFileInput(attrs={'class': 'form-control'}),
        }
    logo = forms.ImageField(widget=ClearableFileInput(), required=False)
