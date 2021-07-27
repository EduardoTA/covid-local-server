from django import forms
from django.forms.fields import URLField
from django.forms.models import ModelForm
from .models import Imunizacao, Paciente
from validate_docbr import CNS as cns1
from validate_docbr import CPF as cpf1

# class PacienteForm(ModelForm):
#     class Meta:
#         model = Paciente
#         fields = [f.name for f in Paciente._meta.get_fields() if ((f.name != 'id') and f.name != 'modificado')]

print([f.name for f in Paciente._meta.get_fields()])

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = [f.name for f in Paciente._meta.get_fields() if ((f.name != 'id') and f.name != 'modificado' and f.name != 'imunizacao')]

class ImunizacaoForm(ModelForm):
    class Meta:
        model = Imunizacao
        fields = [f.name for f in Imunizacao._meta.get_fields() if ((f.name != 'id') and f.name != 'modificado')]
        