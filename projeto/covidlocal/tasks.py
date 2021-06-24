from time import sleep
from .models import Paciente
from django.core import serializers
import requests

def sincronizar():
    numero_de_pacientes = Paciente.objects.all().count()
    for i in range(0,numero_de_pacientes):
        serialized_obj = serializers.serialize('json', [ Paciente.objects.get(id=i+1), ])
        requests.post('http://127.0.0.1:5000', serialized_obj)