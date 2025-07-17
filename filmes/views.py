from filmes.models import Filme
from rest_framework import generics
from filmes.serializers import FilmeSerializer



class FilmeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class FilmeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
