# Generated by Django 4.0.6 on 2022-07-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0014_colab_uf_colabfomacao_colabnivelform_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colabstatus',
            name='descricao',
            field=models.CharField(choices=[('afastado', 'AFASTADO'), ('ativo', 'ATIVO'), ('contrato encerrado', 'CONTRATO ENCERRADO'), ('exonerado', 'EXONERADO')], max_length=50, verbose_name='Descrição do Status'),
        ),
    ]
