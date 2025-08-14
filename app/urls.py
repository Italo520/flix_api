from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Flix API",
      default_version='v1',
      description="Uma API para gerenciar filmes, gêneros, atores e reviews.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@flixapi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('autenticacao.urls')),
    path('api/v1/', include('generos.urls')),
    path('api/v1/', include('filmes.urls')),
    path('api/v1/', include('atores.urls')),
    path('api/v1/', include('reviews.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]