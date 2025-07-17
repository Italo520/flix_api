from django.urls import path
from . import views


urlpatterns = [

    path('atores/',views.AtoresListCreateAPIView.as_view(), name='criar-listar-atores'),
    path('atores/<int:pk>/',views.AtoresRetrieveUpdateDestroyAPIView.as_view(), name='detalhe-ator-view'),

]