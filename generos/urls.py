from django.urls import path
from . import views

urlpatterns = [

    path('generos/', views.GeneroListaCriarAPIView.as_view(), name='criar-listar-generos'),
    path('generos/<int:pk>/', views.GeneroRetrieveUpdateDestroiAPIView.as_view(), name='detalhe-genero-view'),

]
