from django.http import request, response
from .api.serializers import ImunizacaoSerializer,PacienteSerializer
from time import sleep
from .models import Paciente,Imunizacao
from rest_framework import serializers
import requests
import json

def sincronizar():
    headers = {'content-type': 'application/json'}
    numero_de_pacientes = Paciente.objects.all().count()
    for i in range(0,numero_de_pacientes):
        paciente = Paciente.objects.all().values()[i]
        #paciente.pop('id')
        serialized_obj = PacienteSerializer(paciente)
        #print(serialized_obj)
        json1 = json.dumps(serialized_obj.data)
        #print(json1)
        response = requests.post('https://serverremoto.herokuapp.com/api/Pacientes/', data=json1,headers=headers)
        #print(json1)



    numero_de_imunizacoes = Imunizacao.objects.all().count()
    for i in range(0,numero_de_imunizacoes):
        imunizacoes = Imunizacao.objects.all().values()[i]
        imunizacoes.pop('id')
        serialized_obj = ImunizacaoSerializer(imunizacoes)
        
        json1 = json.dumps(serialized_obj.data)
        response = requests.post('https://serverremoto.herokuapp.com/api/Imunizacoes/', data=json1,headers=headers)
        print(json1)