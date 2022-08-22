from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all().order_by('id')
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'nome', 'descricao', 'idade_minima']