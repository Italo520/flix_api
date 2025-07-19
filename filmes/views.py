from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from filmes.models import Filme
from filmes.serializers import FilmeSerializer



class FilmeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer



class FilmeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
