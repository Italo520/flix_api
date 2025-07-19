from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView





urlpatterns = [

    path('autenticacao/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('autenticacao/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('autenticacao/token/verify/', TokenVerifyView.as_view(), name='token-verify'),


]