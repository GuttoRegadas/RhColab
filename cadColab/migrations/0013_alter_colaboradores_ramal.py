# Generated by Django 4.0.6 on 2022-07-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0012_alter_colaboradores_tel_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='ramal',
            field=models.CharField(blank=True, max_length=12, verbose_name='Ramal'),
        ),
    ]