from django.db import models
from generos.models import Genero
from atores.models import Atores


class Filme(models.Model):
    titulo = models.CharField(max_length=500)   
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    ano_lancamento = models.DateField(null=True, blank=True)
    atores = models.ManyToManyField(Atores, related_name='filmes')
    sinopse = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.titulo