from django import forms

from .models import Paciente

class PacienteForm(forms.Form):
    # class Meta:
    #     model = Paciente
    #     fields = [
    #         'id',
    #         'id_cand',
    #         'isCNS',
    #         'nome',
    #         'nomeMae',
    #         'nomeSocial',
    #         'dataNascimento',
    #         'sexo',
    #         'raca',
    #         'telefone',
    #         'gestante',
    #         'puerpera',
    #         'pais',
    #         'UF',
    #         'municipio',
    #         #'zona',
    #         'logradouro',
    #         'numero',
    #         'bairro',
    #         'complemento',
    #         'email'
    #     ]
    CPF = forms.IntegerField(label = 'CPF')
    CNS = forms.IntegerField(label = 'CNS')

    sexos = (
        ("FEMININO", "Feminino"),
        ("MASCULINO", "Masculino"),
        ("IGNORADO", "Ignorado")
    )

    racas = (
        ("AMARELA", "AMARELA"),
        ("BRANCA", "BRANCA"),
        ("INDIGENA", "INDIGENA"),
        ("NAO INFORMADA", "NAO INFORMADA"),
        ("PARDA", "PARDA"),
        ("PRETA", "PRETA")
    )

    zonas = (
        ("RURAL", "RURAL"),
        ("URBANA", "URBANA")
    )

    nome = forms.CharField(label = 'Nome')
    nomeMae = forms.CharField(label = 'Nome da Mãe')
    nomeSocial = forms.CharField(label = 'Nome Social')
    dataNascimento = forms.IntegerField(label = 'Data de Nascimento')
    sexo = forms.CharField(label = 'Sexo')
    raca = forms.CharField(label = 'Raça')
    telefone = forms.IntegerField(label = 'Telefone')
    gestante = forms.BooleanField(label = 'Gestante')
    puerpera = forms.BooleanField(label = 'Puérpera')
    pais = forms.CharField(label = 'País')
    UF = forms.CharField(label = 'UF')
    municipio = forms.CharField(label = 'Município')
    zona = forms.CharField(label = 'Zona')
    logradouro = forms.CharField(label = 'Logradouro')
    numero = forms.IntegerField(label = 'Número')
    bairro = forms.CharField(label = 'Bairro')
    complemento = forms.CharField(label = 'Complemento')
    email = forms.CharField(label = 'E-mail')
