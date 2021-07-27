from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _
import datetime
from validate_docbr import CNS as cns1
from validate_docbr import CPF as cpf1

from .choices import * 

# Campo customizado que converte uma string vazia ('') para None
class EmptyStringToNoneField(models.CharField):
    def get_prep_value(self, value):
        if value == '':
            return None  
        return value

# Modelo para Paciente
class Paciente(models.Model):
    CPF = EmptyStringToNoneField(null=True,blank=True, default=None, unique=True, max_length=11, verbose_name='CPF')
    CNS = EmptyStringToNoneField(null=True,blank=True, default=None, unique=True, max_length=15, verbose_name='CNS')

    nome = models.CharField(max_length=100, verbose_name='Nome')
    nomeMae = models.CharField(max_length=100, verbose_name='Nome da Mãe')
    nomeSocial = models.CharField(max_length=100, blank=True, verbose_name='Nome Social')
    dataNascimento = models.DateField(verbose_name='Data de Nascimento (dd/mm/aaaa)')
    sexo = models.CharField(max_length=10, choices=get_choices('sexos'), verbose_name='Sexo')
    raca = models.CharField(max_length=20, choices=get_choices('racas'), verbose_name='Raça')
    telefone = models.IntegerField(verbose_name='Telefone')
    gestante = models.BooleanField(verbose_name='Gestante')
    puerpera = models.BooleanField(verbose_name='Puérpera')
    pais = models.CharField(default='BR', max_length=100, verbose_name='País', choices=get_choices('paises'))
    UF = models.CharField(max_length=2, choices=get_choices('estados'), verbose_name='UF')
    municipio = models.CharField(max_length=100, verbose_name='Município')
    zona = models.CharField(max_length=6, choices=get_choices('zonas'), verbose_name='Zona')
    logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    numero = models.IntegerField(verbose_name='Número')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    complemento = models.CharField(max_length=10, blank=True, verbose_name='Complemento')
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    modificado = models.BooleanField()
    
    def __str__(self):
        return str('CPF: '+str(self.CPF)+', Nome: '+self.nome)

# Modelo para Imunobiológico
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

# Modelo para Lote
class Lote(models.Model):
    lote = models.CharField(max_length=100)
    imunobiologico = models.ForeignKey(Imunobiologico, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Imunobiológico")
    validade = models.DateField(null=True, verbose_name="Data de Validade do Lote")

    def __str__(self):
        return str('Lote: '+str(self.lote)+', imuno.: '+self.imunobiologico.imunobiologico + ', val.: ' + str(self.validade))

# Modelo para Imunização
class Imunizacao(models.Model):
    doses = (
        ("UNICA","UNICA"),
        ("1º DOSE","1º DOSE"),
        ("2º DOSE","2º DOSE")
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Paciente")
    
    comorbidades = MultiSelectField(default=None, blank=True,choices = get_choices('comorbidades'), verbose_name="Comorbidades") # Se grupo=COMORBIDADE
    CRM_medico_resp = models.IntegerField(null=True, default=None, blank=True, verbose_name="CRM médico responsável") # Se grupo=COMORBIDADE
    
    num_BPC = models.IntegerField(null=True, default=None, blank=True, verbose_name="Número do BPC") # Se grupo=PESSOA COM DEFICIENCIA PERMANENTEMENTE SEVERA

    dose = models.CharField(max_length=16, choices=doses, verbose_name="Dose")
    imunobiologico = models.ForeignKey(Imunobiologico, on_delete=models.CASCADE, blank=False, default=None, verbose_name="Imunobiológico")
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=False, default=None, verbose_name="Lote")

    via_admn = models.CharField(max_length=20, choices=get_choices('vias_admn'), verbose_name="Via de Administração")
    local_admn = models.CharField(max_length=20, choices=get_choices('locais_admn'), verbose_name="Local de Administração")

    vacinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        default=None,
        verbose_name="Vacinador"
    )

    grupo = models.CharField(max_length=100, choices=get_choices('grupos'), verbose_name="Grupo de Atendimento")

    estrategia = models.CharField(max_length=100, choices=get_choices('estrategias'), verbose_name="Estratégia")
    
    data_aplic = models.DateField(null=True, verbose_name="Data de Aplicação")
    data_apraz = models.DateField(null=True, blank=True, verbose_name="Data de Aprazamento")

    estado_1_dose = models.CharField(null=True, blank=True, max_length=100, choices=get_choices('estados'), verbose_name="Estado Primeira Dose")
    pais_1_dose = models.CharField(null=True, blank=True, max_length=100, choices=get_paises_exceto_brasil(), verbose_name="País Primeira Dose")
    modificado = models.BooleanField()

    def clean(self, *args, **kwargs):
        errors = {} # Dict que armezena os erros para cada campo

        # Esta função adiciona a mensagem de erro e o campo correspondente ao dict 'errors'
        def appendError(field, msg):
            if field in errors:
                errors[field].append(msg)
            else:
                errors[field] = [msg]

        # Se grupo não for 'COMORBIDADE', atribuir nenhuma comorbidade automaticamente
        if self.grupo != "COMORBIDADE":
            self.comorbidades = ''

        # Exceção se comorbidades forem escolhidas e grupo do paciente não é "COMORBIDADE"
        if len(self.comorbidades) != 0 and self.grupo != "COMORBIDADE":
            appendError('comorbidades', _("Campo 'Comorbidades' somente se paciente for do grupo 'COMORBIDADE'"))
        
        # Exceção se houver número de CRM de médico e grupo do paciente não é "COMORBIDADE"
        if self.CRM_medico_resp != None and self.grupo != "COMORBIDADE":
            appendError('CRM_medico_resp', _("Campo 'CRM_medico_resp' somente se paciente for do grupo 'COMORBIDADE'"))

        # Exceção se houver número BPC de médico e grupo do paciente não é "PESSOA COM DEFICIENCIA PERMANENTE SEVERA"
        if self.num_BPC != None and self.grupo != "PESSOA COM DEFICIENCIA PERMANENTE SEVERA":
            appendError('num_BPC', _("Campo 'Número BPC' somente se paciente for do grupo 'PESSOA COM DEFICIENCIA PERMANENTE SEVERA'"))
        

        # Se estado de 1ª dose ou país de 1ª dose estiverem preenchidos e for 1ª dose, exceção
        if (self.estado_1_dose != None or self.pais_1_dose != None) and self.dose == "1º DOSE":
            appendError('dose', _("1ª dose já foi tomada em outro país ou estado"))

        # Verificações que dependem de imunobiologico != None, ou seja, foi escolhido um imunobiológico
        #if self.imunobiologico != None:
        try:
            # Exceção se dose não for UNICA para imunobiologico de dose única
            if int(self.imunobiologico.doses) == 1 and self.dose != "UNICA":
                appendError('dose', _("Campo 'Dose' só pode ter valor 'UNICA' para imunobiológico de dose única"))
            
            # Exceção se dose = UNICA para imunobiologico de 2 doses
            if int(self.imunobiologico.doses) == 2 and self.dose == "UNICA":
                appendError('dose', _("Campo 'Dose' não pode ter valor 'UNICA' para imunobiológico de 2 doses"))
            
            # Exceção se imunobiológico de dose única e houver uma data de aprazamento
            if int(self.imunobiologico.doses) == 1 and self.data_apraz != None:
                appendError('data_apraz', _("Não pode haver data de aprazamento para imunobiológico de dose única"))
            
            # Exceção se for 2ª dose e houver data de aprazamento
            if self.dose == "2º DOSE" and self.data_apraz != None:
                appendError('data_apraz', _("Não pode haver data de aprazamento para 2ª dose"))
            
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
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str('CPF: '+str(self.paciente.CPF)+', Nome: '+self.paciente.nome + ', Imuno.: ' + self.imunobiologico.imunobiologico + ', dose: ' + self.dose)

class AtualizaServer(models.Model):
    data_atualizacao = models.DateTimeField(verbose_name="Última Atualização")
    versao_local = models.DateTimeField(verbose_name="Versão Local")

    class Meta:
        verbose_name_plural = 'Atualiza Server'