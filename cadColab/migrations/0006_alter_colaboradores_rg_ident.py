# Generated by Django 4.0.6 on 2022-07-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0005_cadrastronovo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='rg_ident',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Identidade'),
        ),
    ]