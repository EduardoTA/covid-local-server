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

# class PacienteForm(ModelForm):
#     class Meta:
#         model = Paciente
#         fields = [f.name for f in Paciente._meta.get_fields() if ((f.name != 'id') and f.name != 'modificado' and f.name != 'imunizacao')]

class PacienteForm(forms.Form):
    CPF = forms.CharField(label = 'CPF', required= False)
    CNS = forms.CharField(label = 'CNS', required= False)

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

    UFs_escolhas = (
        ("", ""),
        ("AC", "AC"),
        ("AL", "AL"),
        ("AM", "AM"),
        ("AP", "AP"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("DF", "DF"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO")
    )

    UF = forms.ChoiceField(label = 'UF', choices=UFs_escolhas, required = False)
    municipio = forms.CharField(label = 'Município')
    logradouro = forms.CharField(label = 'Logradouro')
    numero = forms.IntegerField(label = 'Número')
    bairro = forms.CharField(label = 'Bairro')
    complemento = forms.CharField(label = 'Complemento', required= False)
    email = forms.EmailField(label = 'E-mail', required= False)

    def clean(self):
        CPF = self.cleaned_data.get("CPF")
        CNS = self.cleaned_data.get("CNS")

        if CPF == '' and CNS == '':
            raise forms.ValidationError({"CPF": "CPF ou CNS devem ser inseridos"})

        if not cpf1().validate(CPF) and not CPF == '':
            raise forms.ValidationError("CPF inválido")

        if not cns1().validate(CNS) and not CNS == '':
            raise forms.ValidationError("CNS inválida")

        sexo = self.cleaned_data.get("sexo")
        gestante = self.cleaned_data.get("gestante")
        puerpera = self.cleaned_data.get("puerpera")

        if sexo == 'FEMININO' or puerpera or gestante:
            if sexo != 'FEMININO':
                raise forms.ValidationError("Apenas pacientes do sexo feminino podem ser puérperas ou gestantes")
            elif puerpera and gestante:
                raise forms.ValidationError("Paciente não pode estar com o campo Gestante e Puérpera marcados ao mesmo tempo")

        telefone = self.cleaned_data.get("telefone")

        if len(str(telefone)) < 10 or len(str(telefone)) > 11:
            raise forms.ValidationError("Digite um número de telefone válido")

        ddds = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']

        if not str(telefone)[:2] in ddds:
            raise forms.ValidationError("Digite um DDD válido")

class ImunizacaoForm(ModelForm):
    class Meta:
        model = Imunizacao
        fields = [f.name for f in Imunizacao._meta.get_fields() if ((f.name != 'id') and f.name != 'modificado')]
        