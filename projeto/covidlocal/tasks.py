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
        paciente.pop('id')
        if paciente.get('modificado'):
            paciente.pop('modificado')
            serialized_obj = PacienteSerializer(paciente)
            json1 = json.dumps(serialized_obj.data)
            response = requests.patch('https://serverremoto.herokuapp.com/api/Pacientes/', data=json1,headers=headers)
            print('\n')
            print('Envio de Paciente:')
            print(json1)
            print(response)
            print('\n')

    numero_de_imunizacoes = Imunizacao.objects.all().count()
    for i in range(0,numero_de_imunizacoes):
        imunizacoes = Imunizacao.objects.all().values()[i]
        imunizacoes.pop('id')
        serialized_obj = ImunizacaoSerializer(imunizacoes)
        json1 = json.dumps(serialized_obj.data)
        response = requests.patch('https://serverremoto.herokuapp.com/api/Imunizacoes/', data=json1,headers=headers)
        print('\n')
        print('Envio de Imunização:')
        print(json1)
        print(response)
        print('\n')

    # response = requests.get('https://serverremoto.herokuapp.com/api/Pacientes/',headers=headers)
    # for element in response.json():
    #     element.pop('id')
    #     if Paciente.objects.filter(CPF__iexact=element.get('CPF')):
    #         Paciente.objects.filter(CPF__iexact=element.get('CPF')).update(modificado=False,**element)
    #         paciente = Paciente.objects.filter(CPF__iexact=element.get('CPF')).values()[0]
    #     elif Paciente.objects.filter(CNS__iexact=element.get('CNS')):
    #         Paciente.objects.filter(CNS__iexact=element.get('CNS')).update(modificado=False,**element)
    #         paciente = Paciente.objects.filter(CPF__iexact=element.get('CNS')).values()[0]
    #     else:
    #         Paciente.objects.create(modificado = False, **element)
    #     print(element)
    #     print('\n')
        


    # response = requests.get('https://serverremoto.herokuapp.com/api/Imunizacoes/', data=json1,headers=headers)
    # print(response.json())