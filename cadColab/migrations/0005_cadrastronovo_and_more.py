# Generated by Django 4.0.6 on 2022-07-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0004_alter_colaboradores_adic_ocup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadrastroNovo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Colaborador')),
                ('cpf', models.CharField(max_length=15, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('chef_imed', models.CharField(max_length=50, verbose_name='Chefia Imediata')),
                ('area', models.CharField(max_length=20, verbose_name='Área')),
                ('vinculo', models.CharField(max_length=20, verbose_name='Vínculo')),
                ('email_pess', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='E-mail Pessoal')),
                ('rg_ident', models.IntegerField(blank=True, unique=True, verbose_name='Indentidade')),
                ('placa_veic', models.CharField(blank=True, max_length=20, verbose_name='Placa do Veículo')),
                ('ramal', models.IntegerField(blank=True, verbose_name='Ramal')),
                ('sala', models.CharField(blank=True, max_length=30, verbose_name='Sala')),
                ('celular', models.IntegerField(blank=True, unique=True, verbose_name='Celular/Whatsapp')),
            ],
        ),
        migrations.RenameField(
            model_name='colaboradores',
            old_name='identidade',
            new_name='rg_ident',
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='model_veic',
            field=models.CharField(blank=True, max_length=30, verbose_name='Modelo do Veículo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='nascimento',
            field=models.DateField(verbose_name='Data Nascimento'),
        ),
    ]