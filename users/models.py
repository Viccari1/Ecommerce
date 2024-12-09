from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_cpf, validate_phone, validate_password

# Create your models here.
class User(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True, validators=[validate_phone])
    role = models.CharField(max_length=10, default='cliente')
    password = models.CharField(max_length=128, validators=[validate_password])

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)

