# Generated by Django 4.0.6 on 2022-07-27 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0016_rename_descricao_colabarea_descricao_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaboradores',
            name='endereco',
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='uf_municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabmunicipio', verbose_name='UF/Município'),
        ),
    ]
