from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _
import datetime

import json

def get_paises_exceto_brasil():
    try:
        with open('projeto/covidlocal/json/paises.json') as f:
            json_data = json.load(f)
            lista = []
            for i in range(0,len(json_data["paises"])):
                if json_data["paises"][i]["nome"] != "Brasil":
                    lista.append(tuple([json_data["paises"][i]["sigla"], json_data["paises"][i]["nome"]]))
        return tuple(lista)
    except:
        try:
            with open('covidlocal/json/paises.json') as f:
                json_data = json.load(f)
                lista = []
                for i in range(0,len(json_data["paises"])):
                    lista.append(tuple([json_data["paises"][i]["sigla"], json_data["paises"][i]["nome"]]))
            return tuple(lista)
        except:
            pass

def get_estados():
    try:
        with open('projeto/covidlocal/json/estados.json') as f:
            json_data = json.load(f)
            lista = []
            for i in range(0,len(json_data["estados"])):
                lista.append(tuple([json_data["estados"][i]["sigla"], json_data["estados"][i]["nome"]]))
        return tuple(lista)
    except:
        try:
            with open('covidlocal/json/estados.json') as f:
                json_data = json.load(f)
                lista = []
                for i in range(0,len(json_data["estados"])):
                    lista.append(tuple([json_data["estados"][i]["sigla"], json_data["estados"][i]["nome"]]))
            return tuple(lista)
        except:
            pass

# def get_imunobiologicos():
#     with open('projeto/covidlocal/json/imunobiologicos.json') as f:
#         json_data = json.load(f)
#         lista = []
#         for i in range(0,len(json_data["imunobiologicos"])):
#             lista.append(tuple([json_data["imunobiologicos"][i]["imunobiologico"], json_data["imunobiologicos"][i]["imunobiologico"]]))
#     return tuple(lista)

# def get_numero_doses_imunobiologico(imunobiologico):
#     with open('projeto/covidlocal/json/imunobiologicos.json') as f: 
#         json_data = json.load(f)
#         for i in range(0,len(json_data["imunobiologicos"])):
#             if json_data["imunobiologicos"][i]["imunobiologico"] == imunobiologico:
#                 return json_data["imunobiologicos"][i]["numero_doses"]
                             

# def get_dias_aprazamento_imunobiologico(imunobiologico):
#     with open('projeto/covidlocal/json/imunobiologicos.json') as f: 
#         json_data = json.load(f)
#         for i in range(0,len(json_data["imunobiologicos"])):
#             if json_data["imunobiologicos"][i]["imunobiologico"] == imunobiologico:
#                 return json_data["imunobiologicos"][i]["dias_aprazamento"]


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
    ("CIRROSE HEPATICA","CIRROSE HEPATICA"),
    ("DIABETES MELLITUS","DIABETES MELLITUS"),
    ("DOENCA NEUROLOGICA CRONICA","DOENCA NEUROLOGICA CRONICA"),
    ("DOENCA RENAL CRONICA","DOENCA RENAL CRONICA"),
    ("DOENCAS CARDIOVASCULARES E CEREBROVASCULARES","DOENCAS CARDIOVASCULARES E CEREBROVASCULARES"),
    ("GESTANTE","GESTANTE"),
    ("HEMOGLOBINOPATIA GRAVE","HEMOGLOBINOPATIA GRAVE"),
    ("HIPERTENSAO","HIPERTENSAO"),
    ("IMUNOSSUPRIMIDO","IMUNOSSUPRIMIDO"),
    ("OBESIDADE GRAVE","OBESIDADE GRAVE"),
    ("PACIENTE ONCOLOGICO","PACIENTE ONCOLOGICO"),
    ("PESSOA VIVENDO COM HIV","PESSOA VIVENDO COM HIV"),
    ("PNEUMOPATIA CRONICA GRAVE","PNEUMOPATIA CRONICA GRAVE"),
    ("PUERPERA","PUERPERA"),
    ("SINDROME DE DOWN","SINDROME DE DOWN"),
    ("TERAPIA RENAL SUBSTITUTIVA/DIALISE","TERAPIA RENAL SUBSTITUTIVA/DIALISE"),
    ("TRANSPLANTADO DE ORGAO SOLIDO E MEDULA OSSEA","TRANSPLANTADO DE ORGAO SOLIDO E MEDULA OSSEA")
)

class EmptyStringToNoneField(models.CharField):
    def get_prep_value(self, value):
        if value == '':
            return None  
        return value

class Paciente(models.Model):
    CPF = EmptyStringToNoneField(null=True,blank=True, default=None, unique=True, max_length=11)
    CNS = EmptyStringToNoneField(null=True,blank=True, default=None, unique=True, max_length=15)

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
    modificado = models.BooleanField()

    def __str__(self):
        return str('CPF: '+str(self.CPF)+', Nome: '+self.nome)

class Imunobiologico(models.Model):
    imunobiologico = models.CharField(max_length=30)
    doses = models.IntegerField()
    dias_prox_dose = models.SmallIntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.imunobiologico)

    def clean(self, *args, **kwargs):
        if self.doses == 1 and self.dias_prox_dose != None:
            raise ValidationError({'dias_prox_dose': _('Para Imunobiologico de dose única, não deve haver data para 2ª dose')})
        elif self.doses == 2 and self.dias_prox_dose == None:
            raise ValidationError({'dias_prox_dose': _('Configurar dias para a 2ª dose')})
        super().clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Perdas(models.Model):
    estabelecimento = models.CharField(max_length=100)
    data = models.DateField()
    imunobiologico = models.ForeignKey(Imunobiologico, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Imunobiológico")
    lote = models.CharField(max_length=100)
    falha_equip = models.IntegerField()
    falha_trans = models.IntegerField()
    falta_energ = models.IntegerField()
    frasc_trans = models.IntegerField()

class Lote(models.Model):
    lote = models.CharField(max_length=100)
    imunobiologico = models.ForeignKey(Imunobiologico, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Imunobiológico")
    validade = models.DateField(null=True, verbose_name="Data de Validade do Lote")

    def __str__(self):
        return str('Lote: '+str(self.lote)+', imuno.: '+self.imunobiologico.imunobiologico + ', val.: ' + str(self.validade))

class Imunizacao(models.Model):
    doses = (
        ("UNICA","UNICA"),
        ("1º DOSE","1º DOSE"),
        ("2º DOSE","2º DOSE")
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Paciente")
    
    comorbidades = MultiSelectField(default=None, blank=True,choices = comorbidades, verbose_name="Comorbidades") # Se grupo=COMORBIDADE
    CRM_medico_resp = models.IntegerField(null=True, default=None, blank=True, verbose_name="CRM médico responsável") # Se grupo=COMORBIDADE
    
    num_BPC = models.IntegerField(null=True, default=None, blank=True, verbose_name="Número do BPC") # Se grupo=PESSOA COM DEFICIENCIA PERMANENTEMENTE SEVERA

    dose = models.CharField(max_length=16, choices=doses, verbose_name="Dose")
    imunobiologico = models.ForeignKey(Imunobiologico, on_delete=models.CASCADE, blank=False, default=None, verbose_name="Imunobiológico")
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Lote")

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
    
    data_aplic = models.DateField(null=True, verbose_name="Data de Aplicação")
    data_apraz = models.DateField(null=True, blank=True, verbose_name="Data de Aprazamento")

    estado_1_dose = models.CharField(null=True, blank=True, max_length=100, choices=get_estados(), verbose_name="Estado Primeira Dose")
    pais_1_dose = models.CharField(null=True, blank=True, max_length=100, choices=get_paises_exceto_brasil(), verbose_name="País Primeira Dose")
    modificado = models.BooleanField()

    def clean(self, *args, **kwargs):
        errors = {}

        # Exceção se comorbidades forem escolhidas e grupo do paciente não é "COMORBIDADE"
        if len(self.comorbidades) != 0 and self.grupo != "COMORBIDADE":
            if 'comorbidades' in errors:
                errors['comorbidades'].append(_("Campo 'Comorbidades' somente se paciente for do grupo 'COMORBIDADE'"))
            else:
                errors['comorbidades'] = [_("Campo 'Comorbidades' somente se paciente for do grupo 'COMORBIDADE'")] 
        
        # Exceção se houver número de CRM de médico e grupo do paciente não é "COMORBIDADE"
        if self.CRM_medico_resp != None and self.grupo != "COMORBIDADE":
            if 'CRM_medico_resp' in errors:
                errors['CRM_medico_resp'].append(_("Campo 'CRM_medico_resp' somente se paciente for do grupo 'COMORBIDADE'"))
            else:
                errors['CRM_medico_resp'] = [_("Campo 'CRM_medico_resp' somente se paciente for do grupo 'COMORBIDADE'")] 

        # Exceção se houver número BPC de médico e grupo do paciente não é "PESSOA COM DEFICIENCIA PERMANENTE SEVERA"
        if self.num_BPC != None and self.grupo != "PESSOA COM DEFICIENCIA PERMANENTE SEVERA":
            if 'num_BPC' in errors:
                errors['num_BPC'].append(_("Campo 'Número BPC' somente se paciente for do grupo 'PESSOA COM DEFICIENCIA PERMANENTE SEVERA'"))
            else:
                errors['num_BPC'] = [_("Campo 'Número BPC' somente se paciente for do grupo 'PESSOA COM DEFICIENCIA PERMANENTE SEVERA'")]
        



        # Se estado de 1ª dose ou país de 1ª dose estiverem preenchidos, então dose automaticamente troca para 2ª
        if (self.estado_1_dose != None or self.pais_1_dose != None) and self.dose == "1º DOSE":
            if 'dose' in errors:
                errors['dose'].append(_("1ª dose já foi tomada em outro país ou estado"))
            else:
                errors['dose'] = [_("1ª dose já foi tomada em outro país ou estado")]

        # Verificações que dependem de imunobiologico != None, ou seja, foi escolhido um imunobiológico
        try:
            # Exceção se dose não for UNICA para imunobiologico de dose única
            if int(self.imunobiologico.doses) == 1 and self.dose != "UNICA":
                if 'dose' in errors:
                    errors['dose'].append(_("Campo 'Dose' não pode ter valor 'UNICA' para imunobiológico que não seja de dose única"))
                else:
                    errors['dose'] = [_("Campo 'Dose' não pode ter valor 'UNICA' para imunobiológico que não seja de dose única")] 
            
            # Exceção se dose = UNICA para imunobiologico de 2 doses
            if int(self.imunobiologico.doses) == 2 and self.dose == "UNICA":
                if 'dose' in errors:
                    errors['dose'].append(_("Campo 'Dose' não pode ter valor 'UNICA' para imunobiológico que não seja de dose única"))
                else:
                    errors['dose'] = [_("Campo 'Dose' não pode ter valor 'UNICA' para imunobiológico que não seja de dose única")] 
            
            # Exceção se imunobiológico de dose única e houver uma data de aprazamento
            if int(self.imunobiologico.doses) == 1 and self.data_apraz != None:
                if 'data_apraz' in errors:
                    errors['data_apraz'].append(_("Não pode haver data de aprazamento para imunobiológico de dose única"))
                else:
                    errors['data_apraz'] = [_("Não pode haver data de aprazamento para imunobiológico de dose única")]
            
            # Exceçãos se for 2ª dose e houver data de aprazamento
            if self.dose == "2º DOSE" and self.data_apraz != None:
                if 'data_apraz' in errors:
                    errors['data_apraz'].append(_("Não pode haver data de aprazamento para 2ª dose"))
                else:
                    errors['data_apraz'] = [_("Não pode haver data de aprazamento para 2ª dose")] 
            
            # Se for 1ª dose...
            if self.dose == "1º DOSE":
                # Verificação data de aprazamento errada...
                # Se não houver data de aprazamento
                if not self.data_apraz:
                    if 'data_apraz' in errors:
                        errors['data_apraz'].append(_("Insira data de aprazamento"))
                    else:
                        errors['data_apraz'] = [_("Insira data de aprazamento")]
                # O if-else abaixo verifica se a data de aprazamento está certa, dado o imunobiológico escolhido
                elif int((self.data_apraz - self.data_aplic).days):
                    data_certa = str(self.data_aplic+datetime.timedelta(days=self.imunobiologico.dias_prox_dose))
                    mensagem = _("Data de Aprazamento errada, a certa é ")+data_certa
                    if int((self.data_apraz - self.data_aplic).days) != int(self.imunobiologico.dias_prox_dose):
                        if 'data_apraz' in errors:
                            errors['data_apraz'].append(mensagem)
                        else:
                            errors['data_apraz'] = [mensagem]
                else:
                    data_certa = str(self.data_aplic+datetime.timedelta(days=self.imunobiologico.dias_prox_dose))
                    mensagem = _("Data de Aprazamento errada, a certa é ")+data_certa
                    if 'data_apraz' in errors:
                        errors['data_apraz'].append(mensagem)
                    else:
                        errors['data_apraz'] = [mensagem]

            # Exceção se imunobiológico do lote escolhido for diferente do imunobiológico da imunização atual
            if str(self.lote.imunobiologico) !=  str(self.imunobiologico.imunobiologico):
                if 'lote' in errors:
                    errors['lote'].append(_("Escolha lote válido para o imunobiologico"))
                else:
                    errors['lote'] = [_("Escolha lote válido para o imunobiologico")]

            # Verificação se se está tentando registrar imunização para imunobiológico de dose única se o paciente
            # já tomou a 1ª dose em outro estado ou país
            if int(self.imunobiologico.doses) == 1 and (self.estado_1_dose != None or self.pais_1_dose != None):
                raise ValidationError(_("Paciente não pode receber dose única, pois possui outra dose registrada"))
        except Exception as e:
            pass
        
        
        # Exceção se for selecionado país e estado de 1ª dose ao mesmo tempo
        if self.estado_1_dose != None and self.pais_1_dose != None:
            if 'estado_1_dose' in errors:
                errors['estado_1_dose'].append(_("Campos 'Estado Primeira Dose' e 'País Primeira Dose' não podem estar preenchidos ao mesmo tempo"))
            else:
                errors['estado_1_dose'] = [_("Campos 'Estado Primeira Dose' e 'País Primeira Dose' não podem estar preenchidos ao mesmo tempo")]
            if 'pais_1_dose' in errors:
                errors['pais_1_dose'].append(_("Campos 'Estado Primeira Dose' e 'País Primeira Dose' não podem estar preenchidos ao mesmo tempo"))
            else:
                errors['pais_1_dose'] = [_("Campos 'Estado Primeira Dose' e 'País Primeira Dose' não podem estar preenchidos ao mesmo tempo")] 


        # Verificação se a pessoa já fez alguma imunização
        if Imunizacao.objects.filter(paciente=self.paciente):
            # Verifica se paciente já tomou vacina de dose única
            if Imunizacao.objects.filter(paciente=self.paciente, dose="UNICA"):
                raise ValidationError("Paciente já recebeu dose única")
            # Caso não tenha tomado vacina de dose única...

            # Verifica se o usuário quer fazer imunização com imunobiológico
            # de dose única, o que não pode
            if self.imunobiologico.doses == 1:
                raise ValidationError("Paciente não pode receber imunobiológico de dose única se já tomou 1ª dose de outro imunobiológico")
            
            # Verifica se paciente já tomou as duas doses
            if len(Imunizacao.objects.filter(paciente=self.paciente)) == 2:
                raise ValidationError("Paciente já recebeu duas doses")
            
            # Verifica se foi escolhida a opção de 2ª dose
            if self.dose != "2º DOSE":
                if 'dose' in errors:
                    errors['dose'].append(_("Escolha a 2ª dose"))
                else:
                    errors['dose'] = [_("Escolha a 2ª dose")]
            
            # Exceção se estado para 1ª dose for escolhido
            if self.estado_1_dose != None:
                if 'estado_1_dose' in errors:
                    errors['estado_1_dose'].append(_("Não selecione 'Estado Primeira Dose'"))
                else:
                    errors['estado_1_dose'] = [_("Não selecione 'Estado Primeira Dose'")]
            
            # Exceção se país para 1ª dose for escolhido
            if self.pais_1_dose != None:
                if 'pais_1_dose' in errors:
                    errors['pais_1_dose'].append(_("Não selecione 'País Primeira Dose'"))
                else:
                    errors['pais_1_dose'] = [_("Não selecione 'País Primeira Dose'")]

            # Query da 1ª dose
            imunizacao_anterior = Imunizacao.objects.filter(paciente=self.paciente, dose="1º DOSE").first()
            
            # Copia valores de alguns campos da 1ª dose
            self.comorbidades = imunizacao_anterior.comorbidades
            self.CRM_medico_resp = imunizacao_anterior.CRM_medico_resp
            self.num_BPC = imunizacao_anterior.num_BPC
            self.grupo = imunizacao_anterior.grupo
            self.estrategia = imunizacao_anterior.estrategia
            self.estado_1_dose = None
            self.pais_1_dose = None

            # Verifica se data de aplicação da 2ª dose é antes da 1ª dose
            if int((imunizacao_anterior.data_aplic - self.data_aplic).days) > 0:
                if 'data_aplic' in errors:
                    errors['data_aplic'].append(_("Data de Aplicação errada"))
                else:
                    errors['data_aplic'] = [_("Data de Aplicação errada")]

        if errors:
            raise ValidationError(errors)
        super().clean(*args, **kwargs)
        #raise ValidationError("Teste")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str('CPF: '+str(self.paciente.CPF)+', Nome: '+self.paciente.nome + ', Imuno.: ' + self.imunobiologico.imunobiologico + ', dose: ' + self.dose)

class AtualizaServer(models.Model):
    data_atualizacao = models.DateTimeField(verbose_name="Última Atualização")
    versao_local = models.DateTimeField(verbose_name="Versão Local")