from rest_framework import viewsets

from .models import Ativos
from .serializers import AtivosSerializer

# Create your views here.


class AtivoSet(viewsets.ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer
