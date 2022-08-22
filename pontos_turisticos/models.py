from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from localizacao.models import Localizacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao)
    comentarios = models.ManyToManyField(Comentario)
    localizacao = models.ForeignKey(
        Localizacao, on_delete=models.CASCADE  # caso deletar a localizacao, o ponto turistico sera excluido
        , null=True, blank=True,
        )
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.nome