from django.db import models
from users.models import User

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='logos', max_length=255, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class ImagemProduto(models.Model):
    imagem = models.ImageField(upload_to='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    estoque = models.IntegerField()
    vendidos = models.IntegerField(default=0)
    imagemprincipal = models.ImageField(upload_to='produtos', max_length=255, null=True)
    imagens = models.ManyToManyField(ImagemProduto, blank=True)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome