# Generated by Django 4.0.6 on 2022-07-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0003_rename_indentidade_colaboradores_identidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='adic_ocup',
            field=models.BooleanField(blank=True, verbose_name='Adic. Ocupacional'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='amb_sala',
            field=models.CharField(blank=True, max_length=30, verbose_name='Sala'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='bairro',
            field=models.CharField(blank=True, max_length=30, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='banco',
            field=models.CharField(blank=True, max_length=3, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='card_vac',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Comprovante de Vacina'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='celular',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Celular/Whatsapp'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cep_end',
            field=models.IntegerField(blank=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='comp_end',
            field=models.CharField(blank=True, max_length=50, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='coord_resp',
            field=models.CharField(blank=True, max_length=30, verbose_name='Coordenador Responsável'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cor_veic',
            field=models.CharField(blank=True, max_length=2, verbose_name='Cor do Veículo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cpf',
            field=models.CharField(max_length=15, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cracha',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='Crachá'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='email_pess',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='E-mail Pessoal'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='fator_rh',
            field=models.CharField(blank=True, max_length=10, verbose_name='Fator Sanguíneo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='foto_pess',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Foto Pessoal'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='identidade',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Indentidade'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='ingresso',
            field=models.DateField(blank=True, verbose_name='Data do Ingresso'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='logradouro',
            field=models.CharField(blank=True, max_length=30, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='marca_veic',
            field=models.CharField(blank=True, max_length=30, verbose_name='Marca do Veículo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='matricula',
            field=models.IntegerField(unique=True, verbose_name='Mátricula'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='model_veic',
            field=models.CharField(blank=True, max_length=30, verbose_name='Modelo do Vepiculo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='municipio',
            field=models.CharField(blank=True, max_length=30, verbose_name='Município'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='num_end',
            field=models.CharField(blank=True, max_length=20, verbose_name='Nº'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='obs',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='orgao_ident',
            field=models.CharField(blank=True, max_length=20, verbose_name='Orgão Espedidor'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='placa_veic',
            field=models.CharField(blank=True, max_length=20, verbose_name='Placa do Veículo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='plano_sau',
            field=models.CharField(blank=True, max_length=50, verbose_name='Plano de Saúde'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='posseFioce',
            field=models.DateField(blank=True, verbose_name='Data da Posse'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='ramal',
            field=models.IntegerField(blank=True, verbose_name='Ramal'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='tel_res',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Telefone Residêncial'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='uf',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='vacinado',
            field=models.BooleanField(blank=True, verbose_name='Vaciando'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='vigenc_bolsa',
            field=models.DateField(blank=True, verbose_name='Data Vigência'),
        ),
    ]
