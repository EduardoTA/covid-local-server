# Generated by Django 3.2.4 on 2021-06-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('id_cand', models.IntegerField(blank=True, default=None, unique=True)),
                ('isCNS', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('nomeMae', models.CharField(max_length=100)),
                ('nomeSocial', models.CharField(blank=True, max_length=100)),
                ('dataNascimento', models.IntegerField()),
                ('sexo', models.CharField(choices=[('FEMININO', 'Feminino'), ('MASCULINO', 'Masculino'), ('IGNORADO', 'Ignorado')], max_length=10)),
                ('raca', models.CharField(choices=[('AMARELA', 'AMARELA'), ('BRANCA', 'BRANCA'), ('INDIGENA', 'INDIGENA'), ('NAO INFORMADA', 'NAO INFORMADA'), ('PARDA', 'PARDA'), ('PRETA', 'PRETA')], max_length=20)),
                ('telefone', models.IntegerField()),
                ('gestante', models.BooleanField()),
                ('puerpera', models.BooleanField()),
                ('pais', models.CharField(max_length=100)),
                ('UF', models.CharField(max_length=2)),
                ('municipio', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
