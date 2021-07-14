from ..models import Imunizacao, Imunobiologico, Paciente, Lote
from django.contrib.auth.models import User
from rest_framework import serializers
from .. import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lote
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ImunizacaoSerializer(serializers.ModelSerializer):
    paciente_CPF = serializers.SerializerMethodField()
    paciente_CNS = serializers.SerializerMethodField()
    imunobiologico = serializers.SerializerMethodField() 
    lote = serializers.SerializerMethodField() 

    class Meta:
        model = models.Imunizacao
        fields = ['paciente_CPF', 'paciente_CNS', 'comorbidades', 'CRM_medico_resp',
                  'num_BPC', 'dose', 'imunobiologico', 'lote', 'via_admn', 'local_admn',
                  'vacinador', 'grupo', 'estrategia', 'data_aplic', 'data_apraz',
                  'estado_1_dose', 'pais_1_dose']
    
    def get_paciente_CPF(self, obj):
        return Paciente.objects.filter(id=obj['paciente_id']).first().CPF

    def get_paciente_CNS(self, obj):
        return Paciente.objects.filter(id=obj['paciente_id']).first().CNS

    def get_imunobiologico(self, obj):
        return Imunobiologico.objects.filter(id=obj['imunobiologico_id']).first().imunobiologico
    
    def get_lote(self, obj):
        return Lote.objects.filter(id=obj['lote_id']).first().lote

class PerdasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perdas
        fields = '__all__'