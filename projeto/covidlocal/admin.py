from django.contrib import admin

from .models import Paciente, Imunizacao, Perdas, Lote, Imunobiologico

admin.site.register(Paciente)
admin.site.register(Imunizacao)
admin.site.register(Perdas)
admin.site.register(Lote)
admin.site.register(Imunobiologico)

# Register your models here.
