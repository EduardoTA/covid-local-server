from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'id',
            'id_cand',
            'isCNS',
            'nome',
            'nomeMae',
            'nomeSocial',
            'dataNascimento',
            'sexo',
            'raca',
            'telefone',
            'gestante',
            'puerpera',
            'pais',
            'UF',
            'municipio',
            #'zona',
            'logradouro',
            'numero',
            'bairro',
            'complemento',
            'email'
        ]