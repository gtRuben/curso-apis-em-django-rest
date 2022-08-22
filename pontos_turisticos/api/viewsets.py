from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows pontos turisticos to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'localizacao__pais']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        
        return queryset

    # def list(self, request, *args, **kwargs):       # GET endpoint
    #     return Response({'teste': 123})
    #     return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # return Response({'Hello': request.data['nome']})
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):     # PUT
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['GET', 'POST'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['GET', 'POST'], detail=False)
    def teste(self, request):
        pass
