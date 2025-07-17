from django.contrib import admin
from atores.models import Atores


@admin.register(Atores)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'nascionalidade')
 
