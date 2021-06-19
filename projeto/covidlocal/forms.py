from django import forms
from .models import Paciente

class PacienteForm(forms.Form):
    CPF = forms.IntegerField(label = 'CPF', required= False)
    CNS = forms.IntegerField(label = 'CNS', required= False)

    sexos_escolhas = (
        ("FEMININO", "Feminino"),
        ("MASCULINO", "Masculino"),
        ("IGNORADO", "Ignorado")
    )

    sexo = forms.ChoiceField(label = 'Sexo',choices = sexos_escolhas)

    racas_escolhas = (
        ("AMARELA", "Amarela"),
        ("BRANCA", "Branca"),
        ("INDIGENA", "Indígena"),
        ("NAO INFORMADA", "Não Informada"),
        ("PARDA", "Parda"),
        ("PRETA", "Preta")
    )

    raca = forms.ChoiceField(label = 'Raça',choices = racas_escolhas)


    zonas_escolhas = (
        ("RURAL", "Rural"),
        ("URBANA", "Urbana")
    )

    zona = forms.ChoiceField(label = 'Zona',choices = zonas_escolhas)


    nome = forms.CharField(label = 'Nome')
    nomeMae = forms.CharField(label = 'Nome da Mãe')
    nomeSocial = forms.CharField(label = 'Nome Social', required= False)
    dataNascimento = forms.DateField(label = 'Data de Nascimento (dd/mm/aaaa)')
    telefone = forms.IntegerField(label = 'Telefone')
    gestante = forms.BooleanField(label = 'Gestante', required= False)
    puerpera = forms.BooleanField(label = 'Puérpera', required = False)
    pais = forms.CharField(label = 'País')
    UF = forms.CharField(label = 'UF')
    municipio = forms.CharField(label = 'Município')
    logradouro = forms.CharField(label = 'Logradouro')
    numero = forms.IntegerField(label = 'Número')
    bairro = forms.CharField(label = 'Bairro')
    complemento = forms.CharField(label = 'Complemento', required= False)
    email = forms.EmailField(label = 'E-mail', required= False)

    def clean(self):
        CPF = self.cleaned_data.get("CPF")
        CNS = self.cleaned_data.get("CNS")
        if CPF == None and CNS == None:
            raise forms.ValidationError("CPF ou CNS devem ser inseridos")

