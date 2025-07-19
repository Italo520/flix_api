from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from app.permissions import GlobalDefaultPermissions
from .models import Atores
from .serializers import AtoresSerializer, AtoresDetailSerializer




class AtoresListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Atores.objects.all()
    serializer_class = AtoresSerializer
  

class AtoresRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Atores.objects.all()
    serializer_class = AtoresDetailSerializer
    lookup_field = 'pk'
