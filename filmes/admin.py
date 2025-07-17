from django.contrib import admin
from filmes.models import Filme


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','genero', 'ano_lancamento', 'sinopse')