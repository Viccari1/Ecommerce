from django.db import models
from users.models import User
from .validators import non_negative, above_4_digits

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='logos', max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[non_negative, above_4_digits])
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0, validators=[non_negative, above_4_digits])
    sold = models.IntegerField(default=0)
    main_image = models.ImageField(upload_to='products', max_length=255, null=True)
    images = models.ManyToManyField(ProductImage, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name