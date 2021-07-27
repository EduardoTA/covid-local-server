from django.contrib import admin

from .models import Paciente, Imunizacao, Lote, Imunobiologico, AtualizaServer

admin.site.register(Paciente)
admin.site.register(Imunizacao)
admin.site.register(Lote)
admin.site.register(Imunobiologico)
admin.site.register(AtualizaServer)
