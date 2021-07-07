from django.contrib import admin

from .models import Paciente, Imunizacao, Perdas

admin.site.register(Paciente)
admin.site.register(Imunizacao)
admin.site.register(Perdas)

# Register your models here.
