from django.contrib import admin

from .models import Paciente
from .models import Imunização
from .models import Perdas

admin.site.register(Paciente)
admin.site.register(Imunização)
admin.site.register(Perdas)

# Register your models here.
