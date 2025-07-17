from rest_framework import generics
from .models import Atores
from .serializers import AtoresSerializer, AtoresDetailSerializer




class AtoresListCreateAPIView(generics.ListCreateAPIView):
    queryset = Atores.objects.all()
    serializer_class = AtoresSerializer
  

class AtoresRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atores.objects.all()
    serializer_class = AtoresDetailSerializer
    lookup_field = 'pk'
