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
    role = forms.ChoiceField(
        choices=[('cliente', 'Cliente'), ('vendedor', 'Vendedor')], initial='cliente',
        widget=forms.RadioSelect,
        label="Qual o tipo de conta você deseja criar? (ESTÁ OPÇÃO NÃO PODE SER MUDADA FUTURAMENTE!)")

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clear_email(self):
        email = self.cleaned_data.get('email')

        try:
            get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise forms.ValidationError('Email não cadastrado!')
        return email

