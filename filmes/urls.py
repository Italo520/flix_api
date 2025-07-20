from django.urls import path
from . import views


urlpatterns = [

    path('filmes/', views.FilmeListCreateAPIView.as_view(), name='criar-listar-filmes'),
    path('filmes/<int:pk>/', views.FilmeDetailAPIView.as_view(), name='detalhe-filme-view'),
    path('filmes/stats/', views.FilmeStatsAPIView.as_view(), name='filme-stats-view'),

]
