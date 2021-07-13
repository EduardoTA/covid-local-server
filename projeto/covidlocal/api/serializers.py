from rest_framework import serializers
from covidlocal import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class ImunizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imunizacao
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lote
        fields = '__all__'

class PerdasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perdas
        fields = '__all__'