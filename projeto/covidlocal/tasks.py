from django.http import request, response
from .api.serializers import ImunizacaoSerializer,PacienteSerializer, AtualizaServerSerializer
from time import sleep
from .models import AtualizaServer, Paciente,Imunizacao,Imunobiologico,Lote
from django.contrib.auth.models import User
from rest_framework import serializers
import requests
import json
from django.contrib import messages

def atualiza_local():
    headers = {'content-type': 'application/json'}
    data = 0
    response = requests.get('https://serverremoto.herokuapp.com/api/Atualizar/', headers=headers)
    json = response.json()
    for element in json:
        element.pop('id')
        data = AtualizaServer.objects.all()[0]
        data.data_atualizacao = element.get('data_atualizacao')
        data.save()



# Método assíncrono que faz a sincronização do banco de dados local com o remoto
def sincronizar():
    print("Sincronizando")
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
            #print(json1)
            
    numero_de_imunizacoes = Imunizacao.objects.all().count()
    for i in range(0,numero_de_imunizacoes):
        imunizacoes = Imunizacao.objects.all().values()[i]
        imunizacoes.pop('id')
        if imunizacoes.get('modificado'):
            imunizacoes.pop('modificado')
            serialized_obj = ImunizacaoSerializer(imunizacoes)
            json1 = json.dumps(serialized_obj.data)
            response = requests.patch('https://serverremoto.herokuapp.com/api/Imunizacoes/', data=json1,headers=headers)
            #print(json1)

    response = requests.get('https://serverremoto.herokuapp.com/api/Pacientes/',headers=headers)
    for element in response.json():
        element.pop('id')
        if Paciente.objects.filter(CPF__iexact=element.get('CPF')) and element.get('CPF') != None:
            Paciente.objects.filter(CPF__iexact=element.get('CPF')).update(modificado=False,**element)
            paciente = Paciente.objects.filter(CPF__iexact=element.get('CPF')).values()[0]
        elif Paciente.objects.filter(CNS__iexact=element.get('CNS')) and element.get('CNS') != None:
            Paciente.objects.filter(CNS__iexact=element.get('CNS')).update(modificado=False,**element)
            paciente = Paciente.objects.filter(CNS__iexact=element.get('CNS')).values()[0]
        else:
            Paciente.objects.create(modificado = False, **element)

    response = requests.get('https://serverremoto.herokuapp.com/api/Imunizacoes/',headers=headers)
    for data in response.json():
        data.pop('id')

        paciente_pk = 0
        imunobiologico_pk = 0
        lote_pk = 0
        vacinador_pk = 0

        paciente_CPF = data.pop('paciente_CPF')
        paciente_CNS = data.pop('paciente_CNS')
        if paciente_CPF:
            paciente_pk = Paciente.objects.filter(CPF=paciente_CPF).first()
        else:
            paciente_pk = Paciente.objects.filter(CNS=paciente_CNS).first()

        imunobiologico = data.pop('imunobiologico')
        imunobiologico_pk = Imunobiologico.objects.filter(imunobiologico=imunobiologico).first()

        lote = data.pop('lote')
        lote_pk = Lote.objects.filter(lote=lote).first()

        vacinador = data.pop('vacinador')
        vacinador_pk = User.objects.filter(username=vacinador).first()

        data['paciente'] = paciente_pk
        data['imunobiologico'] = imunobiologico_pk
        data['lote'] = lote_pk
        data['vacinador'] = vacinador_pk

        if Imunizacao.objects.filter(paciente__exact=data['paciente']).filter(dose__exact=data['dose']):
            Imunizacao.objects.filter(paciente__exact=data['paciente']).filter(dose__exact=data['dose']).update(modificado=False,**data)
            imunizacao = Imunizacao.objects.filter(paciente__exact=data['paciente']).filter(dose__exact=data['dose'])[0]
        else:
            imunizacao = Imunizacao.objects.create(modificado=False,**data)