from django.db import models
from django.conf import settings

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

estratégias = (
    ("CAMPANHA INDISCRIMINADA", "CAMPANHA INDISCRIMINADA"),
)

estados = (

)

paises = (

)

class Paciente(models.Model):
    CPF = models.IntegerField(null=True,blank=True, default=None, unique=True)
    CNS = models.IntegerField(null=True,blank=True, default=None, unique=True)

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
    UF = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    zona = models.CharField(max_length=6, choices=zonas)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.CPF)

class Lote(models.Model):
    lote = models.CharField(max_length=100)
    imunobiologico = models.CharField(max_length=18, choices=imunobiologicos)

class Imunização(models.Model):
    doses = (
        (1,"1ª dose"),
        (2,"2ª dose")
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    dose = models.IntegerField(choices=doses)
    imunobiologico = models.CharField(max_length=18, choices=imunobiologicos)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=True, default=None)

    via_admn = models.CharField(max_length=20, choices=vias_admn)
    local_admn = models.CharField(max_length=20, choices=locais_admn)

    vacinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        default=None
    )

    grupo = models.CharField(max_length=100, choices=grupos)

    estratégia = models.CharField(max_length=100, choices=estratégias)
    
    data_aplic = models.DateField()
    data_apraz = models.DateField(blank=True)

    estado_1_dose = models.TextField(max_length=100, choices=estados)
    pais_1_dose = models.TextField(max_length=100, choices=paises)

class Perdas(models.Model):
    estabelecimento = models.CharField(max_length=100)
    data = models.DateField()
    imunobiologico = models.CharField(max_length=18, choices=imunobiologicos)
    lote = models.CharField(max_length=100)
    falha_equip = models.IntegerField()
    falha_trans = models.IntegerField()
    falta_energ = models.IntegerField()
    frasc_trans = models.IntegerField()