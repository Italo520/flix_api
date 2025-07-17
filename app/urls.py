from django.contrib import admin
from django.urls import path
from generos.views import GeneroListaCriarAPIView, GeneroRetrieveUpdateDestroiAPIView
from atores.views import AtoresListCreateAPIView, AtoresRetrieveUpdateDestroyAPIView
from filmes.views import FilmeListCreateAPIView, FilmeDetailAPIView
from reviews.views import ReviewListCreateAPIView, ReviewDetailAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('generos/',GeneroListaCriarAPIView.as_view(), name= 'criar-listar-generos'),
    path('generos/<int:pk>/',GeneroRetrieveUpdateDestroiAPIView.as_view() , name='detalhe-genero-view'),

    path('atores/',AtoresListCreateAPIView.as_view(), name='criar-listar-atores'),
    path('atores/<int:pk>/',AtoresRetrieveUpdateDestroyAPIView.as_view(), name='detalhe-ator-view'),

    path('filmes/', FilmeListCreateAPIView.as_view(), name='criar-listar-filmes'),
    path('filmes/<int:pk>/', FilmeDetailAPIView.as_view(), name='detalhe-filme-view'),

    path('reviews/', ReviewListCreateAPIView.as_view(), name='criar-listar-reviews'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='detalhe-review-view'),
]
