# Generated by Django 4.0.6 on 2022-07-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadColab', '0006_alter_colaboradores_rg_ident'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='banco',
            field=models.CharField(blank=True, choices=[('654', 'A.J. RENNER S.A.'), ('246', 'ABC-BRASIL S.A.'), ('213', 'ARBI S.A.'), ('25', 'BANCO ALFA'), ('241', 'Banco Classico S.A'), ('83', 'BANCO DA CHINA BRASIL S.A.'), ('300', 'BANCO DE LA NACION ARGENTINA'), ('495', 'BANCO DE LA PROVINCIA DE BUENOS AIRES'), ('494', 'BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY'), ('1', 'BANCO DO BRASIL'), ('37', 'BANCO DO ESTADO DO PARÁ S.A'), ('456', 'BANCO TOKYO MITSUBISH UFJ BRASIL S.A'), ('370', 'BANCO WESTLB DO BRASIL'), ('756', 'BANCOOB'), ('756', 'BANCOOB'), ('47', 'BANESE'), ('33', 'BANESPA'), ('21', 'BANESTES'), ('719', 'BANIF-BANCO INTERNACIONAL DO FUNCHAL (BRASIL) S.A'), ('755', 'BANK OF AMERICA MERRILL LYNCH BANCO MULTIPLO S.A.'), ('41', 'BANRISUL'), ('740', 'BARCLAYS S.A.'), ('3', 'BASA'), ('107', 'BBM S.A'), ('81', 'BBN BANCO BRASILEIRO DE NEGOCIOS S.A'), ('250', 'BCV - BANCO DE CREDITO E VAREJO S.A'), ('36', 'BEM'), ('122', 'BERJ S.A'), ('78', 'BES INVESTIMENTO DO BRASIL SA - BANCO DE INVESTIM.'), ('739', 'BGN S.A.'), ('320', 'BIC BANCO'), ('394', 'BMC S.A.'), ('394', 'BMC S.A.'), ('96', 'BM&F DE SERV. DE LIQUIDACAO E CUSTODIA S.A'), ('394', 'BMC S.A.'), ('318', 'BMG S.A.'), ('4', 'BNB'), ('752', 'BNP PARIBAS BRASIL S.A'), ('17', 'BNY MELLON S.A.'), ('248', 'BOA VISTA INTERATLANTICO S.A'), ('218', 'BONSUCESSO S.A.'), ('69', 'BPN BRASIL BANCO MULTIPLO S.A'), ('65', 'BRACCE S.A.'), ('237', 'BRADESCO'), ('225', 'BRASCAN S.A.'), ('125', 'BRASIL PLURAL S.A. BANCO MULTIPLO'), ('70', 'BRB'), ('92', 'BRICKELL S A CREDITO, FINANCIAMENTO E INVESTIMENTO'), ('208', 'BTG PACTUAL S.A.'), ('263', 'CACIQUE S.A.'), ('104', 'CAIXA ECON. FEDERAL'), ('473', 'CAIXA GERAL - BRASIL S.A.'), ('412', 'CAPITAL S.A.'), ('40', 'CARGILL S.A'), ('112', 'CC UNICRED BRASIL CENTRAL'), ('84', 'CC UNIPRIME NORTE DO PARANA'), ('114', 'CECOOPES-CENTRAL DAS COOP DE ECON E CRED MUTUO DO'), ('85', 'CECREDI'), ('266', 'CEDULA S.A.'), ('233', 'CIFRA S.A.'), ('745', 'CITIBANK'), ('477', 'Citibank N.A.'), ('90', 'COOPERATIVA CENTRAL DE CREDITO DO ESTADO DE SP'), ('97', 'COOPERATIVA CENTRAL DE CREDITO NOROESTE BRASILEIRO'), ('89', 'COOPERATIVA DE CREDITO RURAL DA REGIAO DA MOGIANA'), ('75', 'CR2 S.A'), ('98', 'CREDIALIANCA COOPERATIVA DE CREDITO RURAL'), ('222', 'CREDIT AGRICOLE BRASIL S.A.'), ('505', 'CREDIT SUISSE (BRASIL) S.A.'), ('707', 'DAYCOVAL'), ('487', 'DEUTSCHE BANK S. A. - BANCO ALEMAO'), ('214', 'DIBENS S.A.'), ('265', 'FATOR S.A.'), ('224', 'FIBRA'), ('626', 'FICSA S.A.'), ('121', 'GERADOR S.A.'), ('612', 'GUANABARA S.A.'), ('62', 'HIPERCARD BANCO MULTIPLO S.A'), ('399', 'HSBC'), ('63', 'IBI'), ('604', 'INDUSTRIAL DO BRASIL S. A.'), ('653', 'INDUSVAL S.A.'), ('492', 'ING BANK N.V.'), ('630', 'INTERCAP S.A.'), ('77', 'INTERMEDIUM S.A.'), ('249', 'Investcred Unibanco'), ('341', 'ITAÚ'), ('652', 'ITAU HOLDING FINANCEIRA S.A'), ('184', 'Itaú-BBA'), ('74', 'J. SAFRA S.A.'), ('376', 'J.P. MORGAN S.A.'), ('217', 'JOHN DEERE S.A.'), ('488', 'JPMORGAN CHASE BANK'), ('76', 'KDB DO BRASIL S.A'), ('757', 'KEB DO BRASIL S.A.'), ('600', 'Luso Brasileiro'), ('243', 'MAXIMA S.A.'), ('389', 'MERCANTIL DO BRASIL'), ('746', 'MODAL S.A.'), ('66', 'MORGAN STANLEY DEAN WITTER S.A'), ('14', 'NATIXIS BRASIL S.A. - BANCO MòLTIPLO'), ('753', 'NBC BANK BRASIL S.A.- BANCO MULTIPLO'), ('45', 'OPPORTUNITY S.A.'), ('79', 'ORIGINAL DO AGRONEGOCIO S.A.'), ('212', 'ORIGINAL S.A.'), ('623', 'PANAMERICANO'), ('254', 'PARANA BANCO S.A.'), ('611', 'PAULISTA'), ('613', 'PECUNIA S.A.'), ('94', 'PETRA S.A.'), ('643', 'PINE S.A.'), ('735', 'POTTENCIAL S.A.'), ('747', 'RABOBANK INTERNATIONAL BRASIL S.A.'), ('88', 'RANDON S.A.'), ('633', 'RENDIMENTO S.A.'), ('741', 'RIBEIRÃO PRETO'), ('120', 'RODOBENS S.A'), ('453', 'RURAL'), ('72', 'RURAL MAIS S.A'), ('422', 'SAFRA'), ('751', 'SCOTIABANK BRASIL S.A BANCO MULTIPLO'), ('743', 'SEMEAR S.A.'), ('748', 'SICREDI'), ('749', 'SIMPLES S.A.'), ('366', 'SOCIETE GENERALE BRASIL S.A'), ('637', 'SOFISA S.A.'), ('464', 'SUMITOMO MITSUI BRASILEIRO S.A.'), ('82', 'TOPAZIO S.A.'), ('634', 'Triangulo'), ('230', 'UNICARD BANCO MULTIPLO S.A'), ('91', 'UNICRED CENTRAL RS - CENTRAL DE COOP ECON CRED MUT'), ('87', 'UNICRED CENTRAL SANTA CATARINA'), ('99', 'UNIPRIME CENTRAL - CENTRAL INT DE COOP DE CRED LTD'), ('655', 'VOTORANTIM'), ('610', 'VR S.A.'), ('119', 'WESTERN UNION DO BRASIL S.A.'), ('124', 'WOORI BANK DO BRASIL S.A')], max_length=3, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='cor_veic',
            field=models.CharField(blank=True, choices=[('1', 'Branco'), ('2', 'Bege'), ('3', 'Amarelo'), ('4', 'Laranja'), ('5', 'Rosa'), ('6', 'Vermelho'), ('7', 'Roxo'), ('8', 'Azul'), ('9', 'Verde'), ('10', 'Marrom'), ('11', 'Preto'), ('12', 'Cinza'), ('13', 'Prata')], max_length=2, verbose_name='Cor do Veículo'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='fator_rh',
            field=models.CharField(blank=True, choices=[('a+', 'A+'), ('b+', 'B+'), ('ab+', 'Ab+'), ('o+', 'O+'), ('a-', 'A-'), ('b-', 'B-'), ('ab-', 'AB-'), ('o-', 'O-')], max_length=10, verbose_name='Fator Sanguíneo'),
        ),
    ]
