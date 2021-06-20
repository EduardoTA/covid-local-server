from django.db import models

class Paciente(models.Model):

    CPF = models.IntegerField(null=True,blank=True, default=None, unique=True, max_length=11)
    CNS = models.IntegerField(null=True,blank=True, default=None, unique=True, max_length=15)

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
