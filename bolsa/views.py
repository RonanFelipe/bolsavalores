from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Ativos, FakeUser
from .serializers import AtivosSerializer, FakeUserSerializer

# Create your views here.


class AtivoSet(viewsets.ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer


class FakeUserSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer
