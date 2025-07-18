from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from filmes.models import Filme
from filmes.serializers import FilmeSerializer



class FilmeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer



class FilmeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
