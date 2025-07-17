from django.contrib import admin
from django.urls import path
from generos.views import GeneroListaCriarAPIView, detalhe_genero_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/',GeneroListaCriarAPIView.as_view(), name= 'criar-listar-generos'),
    path('generos/<int:pk>/',detalhe_genero_view , name='detalhe-genero-view'),
]
