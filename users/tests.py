from django.test import TestCase
from rolepermissions.roles import get_user_roles, assign_role
from users.models import User

# Create your tests here.
user = User.objects.get(username='viccari_loja')
print(user.username)
print(user.first_name)
print(user.last_name)
print(user.cpf)
print(user.email)
print(user.phone)
print(user.role)
print(get_user_roles(user))
print(user.password)