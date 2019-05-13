from rest_framework import serializers

from .models import Ativos


class AtivosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ativos
        fields = ('id', 'nome', 'codigo', 'descricao', 'preco', 'quantidade')
