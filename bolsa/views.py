from rest_framework import viewsets

from .models import Ativos, FakeUser, CompraAtivos
from .serializers import AtivosSerializer, FakeUserSerializer, CompraSerializer

# Create your views here.


class AtivoSet(viewsets.ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer


class FakeUserSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer


class CompraSet(viewsets.ModelViewSet):
    queryset = CompraAtivos
    serializer_class = CompraSerializer
