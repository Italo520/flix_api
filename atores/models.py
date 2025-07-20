from django.db import models


CONST_NASCIONALIDADE = (
    ('BR', 'Brasileiro'),
    ('US', 'Americano'),
    ('FR', 'Francês'),
    ('ES', 'Espanhol'),
    ('IT', 'Italiano'),
    ('JP', 'Japonês'),
    ('CN', 'Chinês'),
    ('IN', 'Indiano'),
    ('DE', 'Alemão'),
    ('RU', 'Russo'),
    ('UK', 'Britânico'),
    ('AU', 'Australiano'),)


class Atores(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    nascionalidade = models.CharField(max_length=50, null=True, blank=True, choices=CONST_NASCIONALIDADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
        ordering = ['nome']  # Ordena os atores pelo nome
