import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()
from covidlocal.models import AtualizaServer
data = AtualizaServer.objects.all()[0]
data.versao_local = data.data_atualizacao
data.save()