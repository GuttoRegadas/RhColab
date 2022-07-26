# Generated by Django 4.0.6 on 2022-07-28 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0019_remove_colabarea_descricao_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colab_uf',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='colaboradores',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='colaboradores',
            name='uf_municipio',
        ),
        migrations.AddField(
            model_name='colab_uf',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do Estado'),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colab_uf', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabmunicipio', verbose_name='Município'),
        ),
        migrations.AlterField(
            model_name='colab_uf',
            name='sigla',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Sigla do Estado'),
        ),
        migrations.AlterField(
            model_name='colabarea',
            name='colabArea',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
        migrations.AlterField(
            model_name='colabbolsa',
            name='colabBolsa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
        migrations.AlterField(
            model_name='colabcargo',
            name='colabCargo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
        migrations.AlterField(
            model_name='colabcoordenador',
            name='colabCoord',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
        migrations.AlterField(
            model_name='colabempresa',
            name='colabEmpresa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
        migrations.AlterField(
            model_name='colabfomacao',
            name='colabFomacao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Formação'),
        ),
        migrations.AlterField(
            model_name='colabmunicipio',
            name='municipio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Município'),
        ),
        migrations.AlterField(
            model_name='colabnivelform',
            name='colabNivelForm',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nível de Formação'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='celular',
            field=models.CharField(blank=True, max_length=25, verbose_name='Celular/Whatsapp'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='coord_resp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadColab.colabcoordenador'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cracha',
            field=models.CharField(blank=True, max_length=30, verbose_name='Crachá'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='genero',
            field=models.CharField(blank=True, choices=[('MC', 'Mulher cisgênera'), ('MT', 'Mulher trans'), ('HC', 'Homem cisgênero'), ('HT', 'Homem trans'), ('NB', 'Pessoa não-binária'), ('NL', 'Nenhuma das opções listadas'), ('NR', 'Prefiro não responder')], max_length=2, verbose_name='Identidade de Gênero'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='logradouro',
            field=models.CharField(max_length=30, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='matricula',
            field=models.CharField(max_length=20, unique=True, verbose_name='Mátricula'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='rg_ident',
            field=models.IntegerField(blank=True, verbose_name='Identidade'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='vacinado',
            field=models.BooleanField(blank=True, verbose_name='Vacinação'),
        ),
        migrations.AlterField(
            model_name='colabstatus',
            name='colabStatus',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Status'),
        ),
        migrations.AlterField(
            model_name='colabvinculo',
            name='colabVinculo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição do Vínculo'),
        ),
    ]
