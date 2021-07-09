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
        requests.post('http://127.0.0.1:5000', serialized_obj)

        print(imuniz.paciente.id)
        parsed = json.loads(serialized_obj)
        print(json.dumps(parsed, indent=4, sort_keys=True))
    # print(serialized_obj)
    # print(imuniz.paciente.id)
    # parsed = json.loads(serialized_obj)
    # print(json.dumps(parsed, indent=4, sort_keys=True))