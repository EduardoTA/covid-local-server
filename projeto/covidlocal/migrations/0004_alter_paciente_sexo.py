# Generated by Django 3.2.4 on 2021-06-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidlocal', '0003_merge_0002_auto_20210618_1810_0002_paciente_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('FEMININO', 'FEMININO'), ('MASCULINO', 'MASCULINO'), ('IGNORADO', 'IGNORADO')], max_length=10),
        ),
    ]
