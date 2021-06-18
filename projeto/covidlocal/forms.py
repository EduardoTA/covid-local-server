from django import forms

from .models import Paciente

class PacienteForm(forms.Form):
    CPF = forms.IntegerField(label = 'CPF')
    CNS = forms.IntegerField(label = 'CNS')

    sexos_escolhas = (
        ("FEMININO", "Feminino"),
        ("MASCULINO", "Masculino"),
        ("IGNORADO", "Ignorado")
    )

    sexo = forms.ChoiceField(label = 'Sexo',choices = sexos_escolhas);

    racas_escolhas = (
        ("AMARELA", "Amarela"),
        ("BRANCA", "Branca"),
        ("INDIGENA", "Indígena"),
        ("NAO INFORMADA", "Não Informada"),
        ("PARDA", "Parda"),
        ("PRETA", "Preta")
    )

    raca = forms.ChoiceField(label = 'Raça',choices = racas_escolhas);


    zonas_escolhas = (
        ("RURAL", "Rural"),
        ("URBANA", "Urbana")
    )

    zona = forms.ChoiceField(label = 'Zona',choices = zonas_escolhas);


    nome = forms.CharField(label = 'Nome')
    nomeMae = forms.CharField(label = 'Nome da Mãe')
    nomeSocial = forms.CharField(label = 'Nome Social')
    dataNascimento = forms.IntegerField(label = 'Data de Nascimento')
    telefone = forms.IntegerField(label = 'Telefone')
    gestante = forms.BooleanField(label = 'Gestante', required= False)
    puerpera = forms.BooleanField(label = 'Puérpera', required = False)
    pais = forms.CharField(label = 'País')
    UF = forms.CharField(label = 'UF')
    municipio = forms.CharField(label = 'Município')
    logradouro = forms.CharField(label = 'Logradouro')
    numero = forms.IntegerField(label = 'Número')
    bairro = forms.CharField(label = 'Bairro')
    complemento = forms.CharField(label = 'Complemento')
    email = forms.CharField(label = 'E-mail')
