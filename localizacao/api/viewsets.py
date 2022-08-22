from rest_framework.viewsets import ModelViewSet
from ..models import Localizacao
from .serializers import LocalizacaoSerializer


class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all().order_by('id')
    serializer_class = LocalizacaoSerializer