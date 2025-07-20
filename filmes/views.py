from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from app.permissions import GlobalDefaultPermissions
from filmes.models import Filme
from reviews.models import Review
from filmes.serializers import FilmeSerializer


class FilmeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeStatsAPIView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()

    def get(self, request):
        total_filmes = self.queryset.count()
        filmes_por_genero = self.queryset.values('genero').annotate(total=Count('id')).order_by('-total')
        total_reviews = Review.objects.count()
        media_avaliacoes = Review.objects.aggregate(avg_estrelas=Avg('estrelas'))['avg_estrelas']

        return response.Response(data={
            'total_filmes': total_filmes,
            'filmes_por_genero': filmes_por_genero,
            'total_reviews': total_reviews,
            'media_avaliacoes': round(media_avaliacoes, 1) if media_avaliacoes else 0,
        }, status=status.HTTP_200_OK)
