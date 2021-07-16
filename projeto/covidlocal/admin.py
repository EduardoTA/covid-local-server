from django.contrib import admin

from .models import Paciente, Imunizacao, Perdas, Lote, Imunobiologico, AtualizaServer

admin.site.register(Paciente)
admin.site.register(Imunizacao)
admin.site.register(Perdas)
admin.site.register(Lote)
admin.site.register(Imunobiologico)
admin.site.register(AtualizaServer)

# Register your models here.
