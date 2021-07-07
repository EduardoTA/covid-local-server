from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField

import json

def get_paises():
    with open('projeto/covidlocal/json/paises.json') as f:
        json_data = json.load(f)
        lista = []
        for i in range(0,len(json_data["paises"])):
            lista.append(tuple([json_data["paises"][i]["sigla"], json_data["paises"][i]["nome"]]))
    return tuple(lista)

def get_estados():
    with open('projeto/covidlocal/json/estados.json') as f:
        json_data = json.load(f)
        lista = []
        for i in range(0,len(json_data["estados"])):
            lista.append(tuple([json_data["estados"][i]["sigla"], json_data["estados"][i]["nome"]]))
    return tuple(lista)

imunobiologicos = (
    ("ASTRAZENECA/OXFORD", "ASTRAZENECA/OXFORD"),
    ("CORONAVAC", "CORONAVAC"),
    ("JANSSEN", "JANSSEN"),
    ("PFIZER", "PFIZER"),
    ("TESTE UNICA", "TESTE UNICA")
)

vias_admn = (
    ("EV", "ENDOVENOSA"),
    ("ID", "INTRADERMICA"),
    ("IM", "INTRAMUSCULAR"),
    ("O", "ORAL"),
    ("SC", "SUBCUTANEA")
)

locais_admn = (
    ("DD", "DELTOIDE DIREITO"),
    ("DE", "DELTOIDE ESQUERDO"),
    ("G", "GLUTEO"),
    ("FL", "LOCAL DO FERIMENTO"),
    ("VLD", "VASTO LATERAL DA COXA DIREITO"),
    ("VLE", "VASTO LATERAL DA COXA ESQUERDA"),
    ("VGD", "VENTROGLUTEO DIREITO"),
    ("VGE", "VENTROGLUTEO ESQUERDO")
)

grupos = (
    ("AEROVIARIOS", "AEROVIARIOS"),
    ("COMORBIDADE", "COMORBIDADE"),
    ("ESTUDO CLINICO", "ESTUDO CLINICO"),
    ("IDOSO", "IDOSO"),
    ("IDOSO EM ILPI", "IDOSO EM ILPI"),
    ("INDIGENAS", "INDIGENAS"),
    ("METROVIARIOS/CPTM", "METROVIARIOS/CPTM"),
    ("MOTORISTAS E COBRADORES DE ONIBUS", "MOTORISTAS E COBRADORES DE ONIBUS"),
    ("PESSOA >= 18 ANOS PORTADORA DE DEFICIENCIA RESIDENTES EM RI", "PESSOA >= 18 ANOS PORTADORA DE DEFICIENCIA RESIDENTES EM RI"),
    ("PESSOA COM DEFICIENCIA", "PESSOA COM DEFICIENCIA"),
    ("PESSOA COM DEFICIENCIA PERMANENTE SEVERA", "PESSOA COM DEFICIENCIA PERMANENTE SEVERA"),
    ("POPULACAO EM GERAL", "POPULACAO EM GERAL"),
    ("POPULACAO EM SITUACAO DE RUA", "POPULACAO EM SITUACAO DE RUA"),
    ("PORTUARIOS", "PORTUARIOS"),
    ("QUILOMBOLA", "QUILOMBOLA"),
    ("RIBEIRINHAS", "RIBEIRINHAS"),
    ("TRABALHADOR DA EDUCACAO", "TRABALHADOR DA EDUCACAO"),
    ("TRABALHADOR DA SEGURANCA PUBLICA", "TRABALHADOR DA SEGURANCA PUBLICA"),
    ("TRABALHADOR DE SAUDE", "TRABALHADOR DE SAUDE")
)

estrategias = (
    ("CAMPANHA INDISCRIMINADA", "CAMPANHA INDISCRIMINADA"),
)

comorbidades = (
    ("Teste", "Teste"),
    ("Teste0", "Teste0")
)

class Paciente(models.Model):
    CPF = models.CharField(null=True,blank=True, default=None, unique=True, max_length=11)
    CNS = models.CharField(null=True,blank=True, default=None, unique=True, max_length=15)

    sexos = (
        ("FEMININO", "FEMININO"),
        ("MASCULINO", "MASCULINO"),
        ("IGNORADO", "IGNORADO")
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

    UFs = (
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

    nome = models.CharField(max_length=100)
    nomeMae = models.CharField(max_length=100)
    nomeSocial = models.CharField(max_length=100, blank=True)
    dataNascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=sexos)
    raca = models.CharField(max_length=20, choices=racas)
    telefone = models.IntegerField()
    gestante = models.BooleanField()
    puerpera = models.BooleanField()
    pais = models.CharField(max_length=100)
    UF = models.CharField(max_length=2, choices=UFs)
    municipio = models.CharField(max_length=100)
    zona = models.CharField(max_length=6, choices=zonas)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.CPF)

class Imunobiológico(models.Model):
    imunobiologico = models.CharField(max_length=20)
    doses = models.SmallIntegerField()
    dias_prox_dose = models.SmallIntegerField(blank=True)

    def __str__(self):
        return str(self.imunobiologico)

    def clean(self, *args, **kwargs):
        if self.doses == 1 and self.dias_prox_dose != None:
            raise ValidationError(_('Para imunobiológico de dose única, não deve haver data para 2ª dose'))
        elif self.doses == 2 and self.dias_prox_dose != None:
            raise ValidationError(_('Configurar dias para a 2ª dose'))
        super().clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Perdas(models.Model):
    estabelecimento = models.CharField(max_length=100)
    data = models.DateField()
    imunobiologico = models.ForeignKey(Imunobiológico, on_delete=models.CASCADE, null=True, blank=True, default=None)
    lote = models.CharField(max_length=100)
    falha_equip = models.IntegerField()
    falha_trans = models.IntegerField()
    falta_energ = models.IntegerField()
    frasc_trans = models.IntegerField()

class Lote(models.Model):
    lote = models.CharField(max_length=100)
    imunobiologico = models.ForeignKey(Imunobiológico, on_delete=models.CASCADE, null=True, blank=True, default=None)

class Imunização(models.Model):
    doses = (
        (1,"1ª dose"),
        (2,"2ª dose")
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="Paciente")
    
    comorbidades = MultiSelectField(choices = comorbidades, verbose_name="Comorbidades")

    dose = models.IntegerField(choices=doses, verbose_name="Dose")
    imunobiologico = models.ForeignKey(Imunobiológico, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="Imunobiológico")
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="Lote")

    via_admn = models.CharField(max_length=20, choices=vias_admn, verbose_name="Via de Administração")
    local_admn = models.CharField(max_length=20, choices=locais_admn, verbose_name="Local de Administração")

    vacinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        default=None,
        verbose_name="Vacinador"
    )

    grupo = models.CharField(max_length=100, choices=grupos, verbose_name="Grupo de Atendimento")

    estrategia = models.CharField(max_length=100, choices=estrategias, verbose_name="Estratégia")
    
    data_aplic = models.DateField(verbose_name="Data de Aplicação")
    data_apraz = models.DateField(blank=True, verbose_name="Data de Aprazamento")

    estado_1_dose = models.TextField(max_length=100, choices=get_estados(), verbose_name="Estado Primeira Dose")
    pais_1_dose = models.CharField(max_length=100, choices=get_paises(), verbose_name="País Primeira Dose")