# Este é o arquivo chamado no batch de iniciação

import os, django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()
from covidlocal.models import AtualizaServer

# Se a tabela AtualizaServer estiver vazia, criar uma entrada
if len(AtualizaServer.objects.all()) == 0:
    AtualizaServer(data_atualizacao=timezone.now(),
                   versao_local=timezone.now()).save()
else:
    pass

data = AtualizaServer.objects.all()[0]
data.versao_local = data.data_atualizacao
data.save()