from django.db import models
from django.utils import timezone

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(
        max_length=50
    )
    sobrenome = models.CharField(
        max_length=50,
        blank=True
    )
    telefone = models.CharField(
        max_length=50
    )
    email = models.CharField(
        max_length=50,
        blank=True
    )
    data_criacao = models.DateTimeField(
        default=timezone.now
    )
    descricao = models.TextField(
        blank=True
    )
    categoria_fk = models.ForeignKey(
        'Categoria',
        on_delete=models.DO_NOTHING

    )
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')


    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.nome



