from django.contrib import admin
from django.urls import path
from generos.views import criar_listar_generos_view, detalhe_genero_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/',criar_listar_generos_view, name= 'criar-listar-generos'),
    path('generos/<int:pk>/',detalhe_genero_view , name='detalhe-genero-view'),
]
