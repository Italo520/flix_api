from django.urls import path
from . import views


urlpatterns = [

    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='criar-listar-reviews'),
    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='detalhe-review-view'),

]