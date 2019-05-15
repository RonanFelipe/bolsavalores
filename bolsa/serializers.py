from rest_framework import serializers

from .models import Ativos, FakeUser, CompraAtivos


class AtivosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ativos
        fields = ('id', 'nome', 'codigo', 'descricao', 'preco', 'quantidade')


class FakeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FakeUser
        fields = ('id', 'name', 'nacionalidade')


class CompraSerializer(serializers.ModelSerializer):
    # user = FakeUserSerializer(read_only=True, many=True)
    # ativos = AtivosSerializer(read_only=True, many=True)

    class Meta:
        model = CompraAtivos
        fields = ('id', 'ativos', 'user')

    # def create(self, validated_data):
    #     compra = FakeUser(
    #         ativos=validated_data['ativos'],
    #         user=validated_data['user']
    #     )
    #     compra.save()
    #     return compra

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = FakeUserSerializer(instance.user).data
        response['ativos'] = AtivosSerializer(instance.ativos).data
        return response
