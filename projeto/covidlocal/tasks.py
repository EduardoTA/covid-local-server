from time import sleep
from .models import Paciente,Imunizacao
from django.core import serializers
import requests
import json

def sincronizar():
    numero_de_imunizacoes = Imunizacao.objects.all().count()
    for i in range(0,numero_de_imunizacoes):
        imuniz = Imunizacao.objects.all()[i]
        serialized_obj = serializers.serialize('json', [ imuniz, Paciente.objects.filter(id = int(imuniz.paciente.id))[0],]) # 
        requests.post('https://serverremoto.herokuapp.com/api/Pacientes/', serialized_obj)
