from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from filmes.models import Filme

class Review(models.Model):
    filme = models.ForeignKey(
        Filme, on_delete=
        models.PROTECT,
        related_name='reviews'
    )

    estrelas= models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser menor que 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser maior que 5 estrelas.'),
        ]
    )

    comentario= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.filme.titulo