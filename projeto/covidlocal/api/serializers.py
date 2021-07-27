from ..models import Imunizacao, Imunobiologico, Paciente, Lote, AtualizaServer
from django.contrib.auth.models import User
from rest_framework import serializers
from .. import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = ['CPF','CNS','nome','nomeMae','nomeSocial','dataNascimento','sexo','raca',
                  'telefone','gestante','puerpera','pais','UF','municipio','zona','logradouro',
                  'numero','bairro','complemento','email']

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lote
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ImunizacaoSerializer(serializers.ModelSerializer):
    paciente_CPF = serializers.SerializerMethodField() # O campo vai ser obtido pelo método 'get_paciente_CPF()'
    paciente_CNS = serializers.SerializerMethodField()
    imunobiologico = serializers.SerializerMethodField() 
    lote = serializers.SerializerMethodField() 
    vacinador = serializers.SerializerMethodField()

    class Meta:
        model = models.Imunizacao
        fields = ['paciente_CPF', 'paciente_CNS', 'comorbidades', 'CRM_medico_resp',
                  'num_BPC', 'dose', 'imunobiologico', 'lote', 'via_admn', 'local_admn',
                  'vacinador', 'grupo', 'estrategia', 'data_aplic', 'data_apraz',
                  'estado_1_dose', 'pais_1_dose'
                 ]
    
    def get_paciente_CPF(self, obj):
        # Retorna o CPF do paciente cujo id é o mesmo do paciente relacionado com a imunização sendo serializada
        return Paciente.objects.filter(id=obj['paciente_id']).first().CPF

    def get_paciente_CNS(self, obj):
        # Retorna o CNS do paciente cujo id é o mesmo do paciente relacionado com a imunização sendo serializada
        return Paciente.objects.filter(id=obj['paciente_id']).first().CNS

    def get_imunobiologico(self, obj):
        # Retorna o nome do imunobiológico cujo id é o mesmo do imunobiológico relacionado com a imunização sendo serializada
        return Imunobiologico.objects.filter(id=obj['imunobiologico_id']).first().imunobiologico
    
    def get_lote(self, obj):
        # Retorna o nome do lote cujo id é o mesmo do lote relacionado com a imunização sendo serializada
        return Lote.objects.filter(id=obj['lote_id']).first().lote
    
    def get_vacinador(self, obj):
        # Retorna o nome do Usuário cujo id é o mesmo do Vacinador relacionado com a imunização sendo serializada
        return User.objects.filter(id=obj['vacinador_id']).first().username

class AtualizaServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtualizaServer
        fields = '__all__'