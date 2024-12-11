from django.test import TestCase
from users.models import User
from .models import Loja
from rolepermissions.roles import assign_role

# Create your tests here.
loja = Loja.objects.get(dono = User.objects.get(username = 'viccari_loja2'))
loja.delete()