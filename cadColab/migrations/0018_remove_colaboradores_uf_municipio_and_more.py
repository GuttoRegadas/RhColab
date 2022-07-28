# Generated by Django 4.0.6 on 2022-07-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0017_remove_colaboradores_endereco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaboradores',
            name='uf_municipio',
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabmunicipio', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='uf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colab_uf', verbose_name='UF'),
        ),
    ]