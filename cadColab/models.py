from django.db import models

# Create your models here.

class Colaborador(models.Model):

#Dados Funcionais

#Obs: A permissão para atualizar esta lista ficará restrita aos administradores do sistema.

    nome = models.CharField(max_length=50, verbose_name="Colaborador")
    status = models.CharField(max_length=1, verbose_name= "Status")#Campo Choices/Extrair o vínculo da planilha/campo obrigatória
    matricula = models.IntegerField(verbose_name= "Mátricula")#se vínculo = servidor é obrigatório
    vinculo = models.CharField(max_length=20, verbose_name="Vínculo")#Extrair o vínculo da planilha/campo obrigatória
    area = models.CharField(max_length=20, verbose_name="Área")#lista obtida no organograma do SGA
    cargo = models.CharField(max_length=30, verbose_name="Cargo")#Lista extraída da planilha,/Obrigatório se vínculo = Servidor
    ingresso = models.DateField(verbose_name="Data do Ingresso")
    posseFioce = models.DateField(verbose_name="Data da Posse")
    empresa = models.CharField(max_length=50, verbose_name="Empresa")#Lista extraída da planilha/Obrigatório se vínculo = Terceirizado
#Obs: Armazenar histórico de alterações
    bolsa = models.CharField(max_length=1, verbose_name="Bolsa")#Lista extraída da planilha/Obrigatório se vínculo = Bolsista
    coord_resp = models.CharField(max_length=30, verbose_name="Coordenador Responsável")#Lista [ RH ], opcional
    vigenc_bolsa = models.DateField(verbose_name="Data Vigência")#Solicitado apenas para Bolsista
    email_pess = models.EmailField(verbose_name="E-mail Pessoal")
    adic_ocup = models.BooleanField(verbose_name="Adic. Ocupacional")
    ramal = models.IntegerField(verbose_name="Ramal")
    cracha = models.CharField(max_length=30, verbose_name="Crachá")
    amb_sala = models.CharField(max_length=30, verbose_name="Sala")#Lista de Salas obtida no Controle de Claviculário
    vacinado = models.BooleanField(verbose_name="Vaciando")
    card_vac = models.ImageField(verbose_name="Comprovante de Vacina")

    #Dados Pessoais
    choices_genero = (
        ("MC", "Mulher cisgênera"),
        ("MT", "Mulher trans"),
        ("HC", "Homem cisgênero"),
        ("HT", "Homem trans"),
        ("NB", "Pessoa não-binária"),
        ("NL", "Nenhuma das opções listadas"),
        ("NR", "Prefiro não responder"))
    choices_uf = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AM", "Amazonas"),
        ("AP", "Amapá"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MG", "Minas Gerais"),
        ("MS", "Mato Grosso do Sul"),
        ("MT", "Mato Grosso"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("PR", "Paraná"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("RS", "Rio Grande do Sul"),
        ("SC", "Santa Catarina"),
        ("SE", "Sergipe"),
        ("SP", "São Paulo"),
        ("TO", "Tocantins"),
    )
    choices_banco = (
        ("654", "A.J. RENNER S.A."),
        ("246", "ABC-BRASIL S.A."),
        ("213", "ARBI S.A."),
        ("25", "BANCO ALFA"),
        ("241", "Banco Classico S.A"),
        ("83", "BANCO DA CHINA BRASIL S.A."),
        ("300", "BANCO DE LA NACION ARGENTINA"),
        ("495", "BANCO DE LA PROVINCIA DE BUENOS AIRES"),
        ("494", "BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY"),
        ("1", "BANCO DO BRASIL"),
        ("37", "BANCO DO ESTADO DO PARÁ S.A"),
        ("456", "BANCO TOKYO MITSUBISH UFJ BRASIL S.A"),
        ("370", "BANCO WESTLB DO BRASIL"),
        ("756", "BANCOOB"),
        ("756", "BANCOOB"),
        ("47", "BANESE"),
        ("33", "BANESPA"),
        ("21", "BANESTES"),
        ("719", "BANIF-BANCO INTERNACIONAL DO FUNCHAL (BRASIL) S.A"),
        ("755", "BANK OF AMERICA MERRILL LYNCH BANCO MULTIPLO S.A."),
        ("41", "BANRISUL"),
        ("740", "BARCLAYS S.A."),
        ("3", "BASA"),
        ("107", "BBM S.A"),
        ("81", "BBN BANCO BRASILEIRO DE NEGOCIOS S.A"),
        ("250", "BCV - BANCO DE CREDITO E VAREJO S.A"),
        ("36", "BEM"),
        ("122", "BERJ S.A"),
        ("78", "BES INVESTIMENTO DO BRASIL SA - BANCO DE INVESTIM."),
        ("739", "BGN S.A."),
        ("320", "BIC BANCO"),
        ("394", "BMC S.A."),
        ("394", "BMC S.A."),
        ("96", "BM&F DE SERV. DE LIQUIDACAO E CUSTODIA S.A"),
        ("394", "BMC S.A."),
        ("318", "BMG S.A."),
        ("4", "BNB"),
        ("752", "BNP PARIBAS BRASIL S.A"),
        ("17", "BNY MELLON S.A."),
        ("248", "BOA VISTA INTERATLANTICO S.A"),
        ("218", "BONSUCESSO S.A."),
        ("69", "BPN BRASIL BANCO MULTIPLO S.A"),
        ("65", "BRACCE S.A."),
        ("237", "BRADESCO"),
        ("225", "BRASCAN S.A."),
        ("125", "BRASIL PLURAL S.A. BANCO MULTIPLO"),
        ("70", "BRB"),
        ("92", "BRICKELL S A CREDITO, FINANCIAMENTO E INVESTIMENTO"),
        ("208", "BTG PACTUAL S.A."),
        ("263", "CACIQUE S.A."),
        ("104", "CAIXA ECON. FEDERAL"),
        ("473", "CAIXA GERAL - BRASIL S.A."),
        ("412", "CAPITAL S.A."),
        ("40", "CARGILL S.A"),
        ("112", "CC UNICRED BRASIL CENTRAL"),
        ("84", "CC UNIPRIME NORTE DO PARANA"),
        ("114", "CECOOPES-CENTRAL DAS COOP DE ECON E CRED MUTUO DO"),
        ("85", "CECREDI"),
        ("266", "CEDULA S.A."),
        ("233", "CIFRA S.A."),
        ("745", "CITIBANK"),
        ("477", "Citibank N.A."),
        ("90", "COOPERATIVA CENTRAL DE CREDITO DO ESTADO DE SP"),
        ("97", "COOPERATIVA CENTRAL DE CREDITO NOROESTE BRASILEIRO"),
        ("89", "COOPERATIVA DE CREDITO RURAL DA REGIAO DA MOGIANA"),
        ("75", "CR2 S.A"),
        ("98", "CREDIALIANCA COOPERATIVA DE CREDITO RURAL"),
        ("222", "CREDIT AGRICOLE BRASIL S.A."),
        ("505", "CREDIT SUISSE (BRASIL) S.A."),
        ("707", "DAYCOVAL"),
        ("487", "DEUTSCHE BANK S. A. - BANCO ALEMAO"),
        ("214", "DIBENS S.A."),
        ("265", "FATOR S.A."),
        ("224", "FIBRA"),
        ("626", "FICSA S.A."),
        ("121", "GERADOR S.A."),
        ("612", "GUANABARA S.A."),
        ("62", "HIPERCARD BANCO MULTIPLO S.A"),
        ("399", "HSBC"),
        ("63", "IBI"),
        ("604", "INDUSTRIAL DO BRASIL S. A."),
        ("653", "INDUSVAL S.A."),
        ("492", "ING BANK N.V."),
        ("630", "INTERCAP S.A."),
        ("77", "INTERMEDIUM S.A."),
        ("249", "Investcred Unibanco"),
        ("341", "ITAÚ"),
        ("652", "ITAU HOLDING FINANCEIRA S.A"),
        ("184", "Itaú-BBA"),
        ("74", "J. SAFRA S.A."),
        ("376", "J.P. MORGAN S.A."),
        ("217", "JOHN DEERE S.A."),
        ("488", "JPMORGAN CHASE BANK"),
        ("76", "KDB DO BRASIL S.A"),
        ("757", "KEB DO BRASIL S.A."),
        ("600", "Luso Brasileiro"),
        ("243", "MAXIMA S.A."),
        ("389", "MERCANTIL DO BRASIL"),
        ("746", "MODAL S.A."),
        ("66", "MORGAN STANLEY DEAN WITTER S.A"),
        ("14", "NATIXIS BRASIL S.A. - BANCO MòLTIPLO"),
        ("753", "NBC BANK BRASIL S.A.- BANCO MULTIPLO"),
        ("45", "OPPORTUNITY S.A."),
        ("79", "ORIGINAL DO AGRONEGOCIO S.A."),
        ("212", "ORIGINAL S.A."),
        ("623", "PANAMERICANO"),
        ("254", "PARANA BANCO S.A."),
        ("611", "PAULISTA"),
        ("613", "PECUNIA S.A."),
        ("94", "PETRA S.A."),
        ("643", "PINE S.A."),
        ("735", "POTTENCIAL S.A."),
        ("747", "RABOBANK INTERNATIONAL BRASIL S.A."),
        ("88", "RANDON S.A."),
        ("633", "RENDIMENTO S.A."),
        ("741", "RIBEIRÃO PRETO"),
        ("120", "RODOBENS S.A"),
        ("453", "RURAL"),
        ("72", "RURAL MAIS S.A"),
        ("422", "SAFRA"),
        ("751", "SCOTIABANK BRASIL S.A BANCO MULTIPLO"),
        ("743", "SEMEAR S.A."),
        ("748", "SICREDI"),
        ("749", "SIMPLES S.A."),
        ("366", "SOCIETE GENERALE BRASIL S.A"),
        ("637", "SOFISA S.A."),
        ("464", "SUMITOMO MITSUI BRASILEIRO S.A."),
        ("82", "TOPAZIO S.A."),
        ("634", "Triangulo"),
        ("230", "UNICARD BANCO MULTIPLO S.A"),
        ("91", "UNICRED CENTRAL RS - CENTRAL DE COOP ECON CRED MUT"),
        ("87", "UNICRED CENTRAL SANTA CATARINA"),
        ("99", "UNIPRIME CENTRAL - CENTRAL INT DE COOP DE CRED LTD"),
        ("655", "VOTORANTIM"),
        ("610", "VR S.A."),
        ("119", "WESTERN UNION DO BRASIL S.A."),
        ("124", "WOORI BANK DO BRASIL S.A"),

    )
    choices_cor_veic = (
        ("1", "Branco"),
        ("2", "Bege"),
        ("3", "Amarelo"),
        ("4", "Laranja"),
        ("5", "Rosa"),
        ("6", "Vermelho"),
        ("7", "Roxo"),
        ("8", "Azul"),
        ("9", "Verde"),
        ("10", "Marrom"),
        ("11", "Preto"),
        ("12", "Cinza"),
        ("13", "Prata"),
    )

    genero = models.CharField(max_length=2, choices=choices_genero, verbose_name="Identidade de Gênero")
    nascimento = models.DateField(verbose_name="Nascimento")
    indentidade = models.IntegerField(verbose_name="Indentidade")
    orgao_ident = models.CharField(max_length=20, verbose_name="Orgão Espedidor")
    tel_res = models.IntegerField(verbose_name="Telefone Residêncial")
    celular = models.IntegerField(verbose_name="Celular/Whatsapp")
    formacao = models.CharField(max_length=50, verbose_name="Formação Acadêmica")#Armazenar histórico de alterações/Separar situação[ concluído, cursando, trancado ]  ( não será incluído no sistema )/Incluir Previsão Finalização ( não será incluído no sistema )
    nivel_form = models.CharField(max_length=50, verbose_name="Nível de Formação")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    uf = models.CharField(max_length=2, choices=choices_uf, verbose_name="UF")
    municipio = models.CharField(max_length=30, verbose_name="Município")
    bairro = models.CharField(max_length=30, verbose_name="Bairro")
    logradouro = models.CharField(max_length=30, verbose_name="Logradouro")
    num_end = models.CharField(max_length=20, verbose_name="Nº")
    comp_end = models.CharField(max_length=50, verbose_name="Complemento")
    cep_end = models.IntegerField(verbose_name="CEP")
    plano_sau = models.CharField(max_length=50, verbose_name="Plano de Saúde")
    fator_rh = models.CharField(max_length=10, verbose_name="Fator Sanguíneo")
    banco = models.CharField(max_length=3, verbose_name="Banco")
    obs = models.TextField(max_length=1000, verbose_name="Observações")
    model_veic = models.CharField(max_length=30, verbose_name="Modelo do Vepiculo")
    marca_veic = models.CharField(max_length=30, verbose_name="Marca do Veículo")
    cor_veic = models.CharField(max_length=2, verbose_name="Cor do Veículo")
    placa_veic = models.CharField(max_length=20)
    foto_pess = models.ImageField(verbose_name="Foto Pessoal")