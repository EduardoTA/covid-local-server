from rest_framework import viewsets
from .. import models
from . import serializers

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()

class ImunizacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Imunizacao.objects.all()
    serializer_class = serializers.ImunizacaoSerializer

class LoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoteSerializer
    queryset = models.Lote.objects.all()

class PerdasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerdasSerializer
    queryset = models.Perdas.objects.all()