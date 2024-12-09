from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    loja = models.ForeignKey('Loja', on_delete=models.CASCADE)
    estoque = models.IntegerField()
    vendidos = models.IntegerField(default=0)
    imagemprincipal = models.ImageField(upload_to='produtos')
    imagens = models.ManyToManyField('ImagemProduto', blank=True)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class ImagemProduto(models.Model):
    imagem = models.ImageField(upload_to='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto.nome

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    dono = models.ForeignKey('users.User', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome