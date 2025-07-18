from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView





urlpatterns = [

    path('autenticacao/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),


]