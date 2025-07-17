from django.contrib import admin
from django.urls import path
from generos.views import GeneroListaCriarAPIView, GeneroRetrieveUpdateDestroiAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/',GeneroListaCriarAPIView.as_view(), name= 'criar-listar-generos'),
    path('generos/<int:pk>/',GeneroRetrieveUpdateDestroiAPIView.as_view() , name='detalhe-genero-view'),
]
