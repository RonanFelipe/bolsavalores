from rest_framework import viewsets

from .models import Ativos, FakeUser
from .serializers import AtivosSerializer, FakeUserSerializer

# Create your views here.


class AtivoSet(viewsets.ModelViewSet):
    queryset = Ativos.objects.filter(status=0)
    serializer_class = AtivosSerializer


class AtivoNotForSale(viewsets.ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer


class FakeUserSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer
