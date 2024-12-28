from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'cpf', 'email', 'phone']
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'cpf': 'CPF',
            'email': 'Email',
            'phone': 'Telefone',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control-password', 'placeholder': 'Senha'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    role = forms.ChoiceField(
        choices=[('client', 'Cliente'), ('seller', 'Vendedor')], initial='client',
        widget=forms.RadioSelect(attrs={'class': 'input-group-pretend'}),
        label="Qual o tipo de conta você deseja criar? (ESTÁ OPÇÃO NÃO PODE SER MUDADA FUTURAMENTE!)")
    
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clear_email(self):
        email = self.cleaned_data.get('email')

        try:
            get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise forms.ValidationError('Email não cadastrado!')
        return email
