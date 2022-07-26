# Generated by Django 4.0.6 on 2022-07-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0010_colabarea_colabbolsa_colabcargo_colabcoordenador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabarea'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='banco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='bolsa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabbolsa'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='card_vac',
            field=models.CharField(blank=True, max_length=255, verbose_name='Comprovante de Vacina'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabcargo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='celular',
            field=models.CharField(blank=True, max_length=25, unique=True, verbose_name='Celular/Whatsapp'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabempresa'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='foto_pess',
            field=models.CharField(blank=True, max_length=255, verbose_name='Foto Pessoal'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabstatus'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='vinculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabvinculo'),
        ),
    ]
