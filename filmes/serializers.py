from django.db.models import Avg
import datetime
from rest_framework import serializers
from filmes.models import Filme


class FilmeSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = '__all__'

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('estrelas'))['estrelas__avg']
        return (
            round(rating, 1) if rating is not None else None
        )

    def validate_ano_lancamento(self, value):
        data_atual = datetime.date.today()
        if value > data_atual:
            raise serializers.ValidationError("O campo data não pode conter uma data futura.")
        return value

    def validate_sinopse(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("A sinopse não pode ter mais de 500 caracteres.")
        return value
