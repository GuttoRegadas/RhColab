from django.db import models

# Create your models here.
class CadrastroNovo(models.Model):

    nome = models.CharField(max_length=50, verbose_name="Colaborador", blank = False, null=False)
    cpf = models.CharField(max_length=15, verbose_name="CPF", blank = False, null=False, unique= True)
    data_nasc = models.DateField(verbose_name="Data de Nascimento", blank = False)
    chef_imed = models.CharField(max_length=50, verbose_name="Chefia Imediata", blank= False, null= False)
    area = models.CharField(max_length=20, verbose_name="Área", blank = False, null=False)#lista obtida no organograma do SGA
    vinculo = models.CharField(max_length=20, verbose_name="Vínculo", blank = False, null=False)#Extrair o vínculo da planilha/campo obrigatória
    email_pess = models.EmailField(verbose_name="E-mail Pessoal" , blank = True, unique= True)
    rg_ident = models.IntegerField(verbose_name="Indentidade", blank = True, unique= True)
    placa_veic = models.CharField(max_length=20, verbose_name="Placa do Veículo", blank = True, null=False)
    ramal = models.IntegerField(verbose_name="Ramal", blank = True)
    sala = models.CharField(max_length=30, verbose_name="Sala", blank = True, null=False)#Lista de Salas obtida no Controle de Claviculário
    celular = models.IntegerField(verbose_name="Celular/Whatsapp", blank = True, unique= True)



class Colaboradores(models.Model):
    
#Dados Funcionais------------------------------------------------------------------------------------------------------------------------------------------------------

    nome = models.CharField(max_length=50, verbose_name="Colaborador", blank = False, null=False)
    status = models.CharField(max_length=1, verbose_name= "Status", blank = False, null=False)#Campo Choices/Extrair o vínculo da planilha/campo obrigatória
    matricula = models.IntegerField(verbose_name= "Mátricula", blank = False, null=False, unique= True)#se vínculo = servidor é obrigatório
    vinculo = models.CharField(max_length=20, verbose_name="Vínculo", blank = False, null=False)#Extrair o vínculo da planilha/campo obrigatória
    area = models.CharField(max_length=20, verbose_name="Área", blank = False, null=False)#lista obtida no organograma do SGA
#Obs: A permissão para atualizar esta lista ficará restrita aos administradores do sistema
    cargo = models.CharField(max_length=30, verbose_name="Cargo", blank = False, null=False)#Lista extraída da planilha,/Obrigatório se vínculo = Servidor
    ingresso = models.DateField(verbose_name="Data do Ingresso", blank = True)
    posseFioce = models.DateField(verbose_name="Data da Posse", blank = True)
    empresa = models.CharField(max_length=50, verbose_name="Empresa", blank = False, null=False)#Lista extraída da planilha/Obrigatório se vínculo = Terceirizado
#Obs: Armazenar histórico de alterações
    bolsa = models.CharField(max_length=1, verbose_name="Bolsa", blank = False, null=False)#Lista extraída da planilha/Obrigatório se vínculo = Bolsista
    coord_resp = models.CharField(max_length=30, verbose_name="Coordenador Responsável", blank = True, null=False)#Lista [ RH ], opcional
    vigenc_bolsa = models.DateField(verbose_name="Data Vigência" , blank = True)#Solicitado apenas para Bolsista
    email_pess = models.EmailField(verbose_name="E-mail Pessoal" , blank = True, unique= True)
    adic_ocup = models.BooleanField(verbose_name="Adic. Ocupacional", blank = True)
    ramal = models.IntegerField(verbose_name="Ramal", blank = True)
    cracha = models.CharField(max_length=30, verbose_name="Crachá", blank = True, null=False, unique= True)
    amb_sala = models.CharField(max_length=30, verbose_name="Sala", blank = True, null=False)#Lista de Salas obtida no Controle de Claviculário
    vacinado = models.BooleanField(verbose_name="Vaciando", blank = True)
    card_vac = models.ImageField(verbose_name="Comprovante de Vacina", blank = True)


#Dados Pessoais---------------------------------------------------------------------------------------------------------------------------------------------------------
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

        ("246", "Banco ABC Brasil S.A."),
        ("748", "Banco Cooperativo Sicredi S.A."),
        ("117", "Advanced Cc Ltda"),
        ("121", "Banco Agibank S.A."),
        ("172", "Albatross Ccv S.A"),
        ("188", "Ativa Investimentos S.A"),
        ("280", "Avista S.A. Crédito, Financiamento e Investimento"),
        ("080", "B&T Cc"),
        ("654", "Banco A.J.Renner S.A."),
        ("246", "Banco ABC Brasil S.A."),
        ("075", "Banco ABN AMRO S.A"),
        ("121", "Banco Agibank S.A."),
        ("025", "Banco Alfa S.A."),
        ("641", "Banco Alvorada S.A."),
        ("065", "Banco Andbank (Brasil) S.A."),
        ("213", "Banco Arbi S.A."),
        ("096", "Banco B3 S.A."),
        ("024", "Banco BANDEPE S.A."),
        ("318", "Banco BMG S.A."),
        ("752", "Banco BNP Paribas Brasil S.A."),
        ("107", "Banco BOCOM BBM S.A."),
        ("063", "Banco Bradescard S.A."),
        ("036", "Banco Bradesco BBI S.A."),
        ("122", "Banco Bradesco BERJ S.A."),
        ("204", "Banco Bradesco Cartões S.A."),
        ("394", "Banco Bradesco Financiamentos S.A."),
        ("237", "Banco Bradesco S.A."),
        ("218", "Banco BS2 S.A."),
        ("208", "Banco BTG Pactual S.A."),
        ("336", "Banco C6 S.A – C6 Bank"),
        ("473", "Banco Caixa Geral – Brasil S.A."),
        ("412", "Banco Capital S.A."),
        ("040", "Banco Cargill S.A."),
        ("368", "Banco Carrefour"),
        ("266", "Banco Cédula S.A."),
        ("739", "Banco Cetelem S.A."),
        ("233", "Banco Cifra S.A."),
        ("745", "Banco Citibank S.A."),
        ("241", "Banco Clássico S.A."),
        ("756", "Banco Cooperativo do Brasil S.A. – BANCOOB"),
        ("748", "Banco Cooperativo Sicredi S.A."),
        ("222", "Banco Credit Agricole Brasil S.A."),
        ("505", "Banco Credit Suisse (Brasil) S.A."),
        ("069", "Banco Crefisa S.A."),
        ("003", "Banco da Amazônia S.A."),
        ("083", "Banco da China Brasil S.A."),
        ("707", "Banco Daycoval S.A."),
        ("051", "Banco de Desenvolvimento do Espírito Santo S.A.	"),
        ("300", "Banco de La Nacion Argentina"),
        ("495", "Banco de La Provincia de Buenos Aires"),
        ("494", "Banco de La Republica Oriental del Uruguay"),
        ("335", "Banco Digio S.A"),
        ("001", "Banco do Brasil S.A."),
        ("047", "Banco do Estado de Sergipe S.A."),
        ("037", "Banco do Estado do Pará S.A."),
        ("041", "Banco do Estado do Rio Grande do Sul S.A."),
        ("004", "Banco do Nordeste do Brasil S.A."),
        ("196", "Banco Fair Corretora de Câmbio S.A"),
        ("265", "Banco Fator S.A."),
        ("224", "Banco Fibra S.A."),
        ("626", "Banco Ficsa S.A."),
        ("094", "Banco Finaxis S.A."),
        ("612", "Banco Guanabara S.A."),
        ("012", "Banco Inbursa S.A."),
        ("604", "Banco Industrial do Brasil S.A."),
        ("653", "Banco Indusval S.A."),
        ("077", "Banco Inter S.A."),
        ("249", "Banco Investcred Unibanco S.A."),
        ("184", "Banco Itaú BBA S.A."),
        ("029", "Banco Itaú Consignado S.A.	"),
        ("479", "Banco ItauBank S.A"),
        ("376", "Banco J. P. Morgan S.A."),
        ("074", "Banco J. Safra S.A."),
        ("217", "Banco John Deere S.A."),
        ("076", "Banco KDB S.A."),
        ("757", "Banco KEB HANA do Brasil S.A."),
        ("600", "Banco Luso Brasileiro S.A."),
        ("243", "Banco Modal S.A."),
        ("066", "Banco Morgan Stanley S.A."),
        ("456", "Banco MUFG Brasil S.A."),
        ("007", "Banco Nacional de Desenvolvimento Econômico e Social – BNDES"),
        ("169", "Banco Olé Bonsucesso Consignado S.A."),
        ("111", "Banco Oliveira Trust Dtvm S.A"),
        ("079", "Banco Original do Agronegócio S.A."),
        ("212", "Banco Original S.A."),
        ("712", "Banco Ourinvest S.A."),
        ("623", "Banco PAN S.A."),
        ("611", "Banco Paulista S.A."),
        ("643", "Banco Pine S.A."),
        ("658", "Banco Porto Real de Investimentos S.A."),
        ("747", "Banco Rabobank International Brasil S.A."),
        ("633", "Banco Rendimento S.A."),
        ("741", "Banco Ribeirão Preto S.A."),
        ("120", "Banco Rodobens S.A."),
        ("422", "Banco Safra S.A."),
        ("033", "Banco Santander (Brasil) S.A."),
        ("743", "Banco Semear S.A."),
        ("754", "Banco Sistema S.A."),
        ("630", "Banco Smartbank S.A."),
        ("366", "Banco Société Générale Brasil S.A."),
        ("637", "Banco Sofisa S.A."),
        ("464", "Banco Sumitomo Mitsui Brasileiro S.A."),
        ("082", "Banco Topázio S.A."),
        ("63", "Banco Triângulo S.A."),
        ("018", "Banco Tricury S.A."),
        ("655", "Banco Votorantim S.A."),
        ("610", "Banco VR S.A."),
        ("119", "Banco Western Union do Brasil S.A."),
        ("124", "Banco Woori Bank do Brasil S.A."),
        ("348", "Banco Xp S/A"),
        ("081", "BancoSeguro S.A."),
        ("021", "BANESTES S.A."),
        ("755", "Bank of America Merrill Lynch Banco Múltiplo S.A."),
        ("268", "Barigui Companhia Hipotecária"),
        ("250", "BCV – Banco de Crédito e Varejo S.A."),
        ("144", "BEXS Banco de Câmbio S.A."),
        ("253", "Bexs Corretora de Câmbio S/A"),
        ("134", "Bgc Liquidez Dtvm Ltda"),
        ("017", "BNY Mellon Banco S.A."),
        ("301", "Bpp Instituição De Pagamentos S.A"),
        ("126", "BR Partners Banco de Investimento S.A."),
        ("070", "BRB – Banco de Brasília S.A."),
        ("092", "Brickell S.A. Crédito, Financiamento e Investimento"),
        ("173", "BRL Trust Distribuidora de Títulos e Valores Mobiliários S.A."),
        ("142", "Broker Brasil Cc Ltda"),
        ("292", "BS2 Distribuidora de Títulos e Valores Mobiliários S.A."),
        ("011", "C.Suisse Hedging-Griffo Cv S.A (Credit Suisse)"),
        ("104", "Caixa Econômica Federal"),
        ("288", "Carol Distribuidora de Títulos e Valor Mobiliários Ltda"),
        ("130", "Caruana Scfi"),
        ("159", "Casa Credito S.A"),
        ("016", "Ccm Desp Trâns Sc E Rs"),
        ("089", "Ccr Reg Mogiana	"),
        ("114", "Central Cooperativa De Crédito No Estado Do Espírito Santo"),
        ("114-7", "Central das Cooperativas de Economia e Crédito Mútuo doEstado do Espírito Santo Ltda."),
        ("320", "China Construction Bank (Brasil) Banco Múltiplo S.A."),
        ("477", "Citibank N.A."),
        ("180", "Cm Capital Markets Cctvm Ltda"),
        ("127", "Codepe Cvc S.A"),
        ("163", "Commerzbank Brasil S.A."),
        ("060", "Confidence Cc S.A"),
        ("085", "Coop Central Ailos"),
        ("085-x", "Cooperativa Central de Crédito Urbano-CECRED"),
        ("090-2", "Cooperativa Central de Economia e Crédito Mutuo – SICOOB UNIMAIS"),
        ("087-6", "Cooperativa Central de Economia e Crédito Mútuo das Unicredsde Santa Catarina e Paraná"),
        ("089-2", "Cooperativa de Crédito Rural da Região da Mogiana"),
        ("286", "Cooperativa de Crédito Rural De Ouro"),
        ("279", "Cooperativa de Crédito Rural de Primavera Do Leste")	,
        ("273", "Cooperativa de Crédito Rural de São Miguel do Oeste – Sulcredi/São Miguel"),
        ("098", "Credialiança Ccr"),
        ("098-1", "CREDIALIANÇA COOPERATIVA DE CRÉDITO RURAL"),
        ("010", "Credicoamo"),
        ("133", "Cresol Confederação"),
        ("182", "Dacasa Financeira S/A"),
        ("707", "Banco Daycoval S.A."),
        ("487", "Deutsche Bank S.A. – Banco Alemão"),
        ("140", "Easynvest – Título Cv S.A"),
        ("149", "Facta S.A. Cfi"),
        ("285", "Frente Corretora de Câmbio Ltda."),
        ("278", "Genial Investimentos Corretora de Valores Mobiliários S.A."),
        ("138", "Get Money Cc Ltda"),
        ("064", "Goldman Sachs do Brasil Banco Múltiplo S.A."),
        ("177", "Guide Investimentos S.A. Corretora de Valores"),
        ("146", "Guitta Corretora de Câmbio Ltda"),
        ("078", "Haitong Banco de Investimento do Brasil S.A."),
        ("062", "Hipercard Banco Múltiplo S.A."),
        ("189", "HS Financeira S/A Crédito, Financiamento e Investimentos"),
        ("269", "HSBC Brasil S.A. – Banco de Investimento")	,
        ("271", "IB Corretora de Câmbio, Títulos e Valores Mobiliários S.A."),
        ("157", "Icap Do Brasil Ctvm Ltda"),
        ("132", "ICBC do Brasil Banco Múltiplo S.A."),
        ("492", "ING Bank N.V."),
        ("139", "Intesa Sanpaolo Brasil S.A. – Banco Múltiplo"),
        ("652", "Itaú Unibanco Holding S.A."),
        ("341", "Itaú Unibanco S.A."),
        ("488", "JPMorgan Chase Bank, National Association"),
        ("399", "Kirton Bank S.A. – Banco Múltiplo"),
        ("293", "Lastro RDV Distribuidora de Títulos e Valores Mobiliários Ltda."),
        ("105", "Lecca Crédito, Financiamento e Investimento S/A"),
        ("145", "Levycam Ccv Ltda"),
        ("113", "Magliano S.A"),
        ("323", "Mercado Pago – Conta Do Mercado Livre"),
        ("128", "MS Bank S.A. Banco de Câmbio"),
        ("137", "Multimoney Cc Ltda"),
        ("014", "Natixis Brasil S.A. Banco Múltiplo"),
        ("191", "Nova Futura Corretora de Títulos e Valores Mobiliários Ltda."),
        ("753", "Novo Banco Continental S.A. – Banco Múltiplo"),
        ("260", "Nu Pagamentos S.A Nubank"),
        ("613", "Omni Banco S.A."),
        ("613", "Omni Banco S.A."),
        ("290", "Pagseguro Internet S.A"),
        ("254", "Paraná Banco S.A."),
        ("326", "Parati – Crédito Financiamento e Investimento S.A."),
        ("194", "Parmetal Distribuidora de Títulos e Valores Mobiliários Ltda"),
        ("174", "Pernambucanas Financ S.A"),
        ("100", "Planner Corretora De Valores S.A"),
        ("125", "Plural S.A. – Banco Múltiplo"),
        ("093", "Pólocred Scmepp Ltda"),
        ("108", "Portocred S.A"),
        ("283", "Rb Capital Investimentos Dtvm Ltda"),
        ("101", "Renascenca Dtvm Ltda"),
        ("270", "Sagitur Corretora de Câmbio Ltda."),
        ("751", "Scotiabank Brasil S.A. Banco Múltiplo"),
        ("276", "Senff S.A. – Crédito, Financiamento e Investimento"),
        ("545", "Senso Ccvm S.A"),
        ("190", "Servicoop"),
        ("183", "Socred S.A"),
        ("299", "Sorocred Crédito, Financiamento e Investimento S.A.	"),
        ("118", "Standard Chartered Bank (Brasil) S/A–Bco Invest."),
        ("197", "Stone Pagamentos S.A"),
        ("340", "Super Pagamentos e Administração de Meios Eletrônicos S.A."),
        ("095", "Travelex Banco de Câmbio S.A."),
        ("143", "Treviso Corretora de Câmbio S.A."),
        ("131", "Tullett Prebon Brasil Cvc Ltda"),
        ("129", "UBS Brasil Banco de Investimento S.A."),
        ("091-", "4	Unicred Central do Rio Grande do Sul"),
        ("91", "Unicred Central Rs"),
        ("136", "Unicred Cooperativa"),
        ("099", "UNIPRIME Central – Central Interestadual de Cooperativas de Crédito Ltda."),
        ("084", "Uniprime Norte do Paraná – Coop de Economia eCrédito Mútuo dos Médicos, Profissionais das Ciências"),
        ("298", "Vips Cc Ltda"),
        ("310", "Vortx Distribuidora de Títulos e Valores Mobiliários Ltda"),
        ("102", "Xp Investimentos S.A"),

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

    choices_fatorRh = (
        ("a+", "A+"),
        ("b+", "B+"),
        ("ab+", "Ab+"),
        ("o+", "O+"),
        ("a-", "A-"),
        ("b-", "B-"),
        ("ab-", "AB-"),
        ("o-", "O-"),
    )

    genero = models.CharField(max_length=2, choices=choices_genero, verbose_name="Identidade de Gênero", null=False)
    cpf = models.CharField(max_length=11, verbose_name="CPF", blank = False, null=False, unique= True)
    nascimento = models.DateField(verbose_name="Data Nascimento", blank = False)
    rg_ident = models.IntegerField(verbose_name="Identidade", blank = True, unique= True)
    orgao_ident = models.CharField(max_length=20, verbose_name="Orgão Espedidor", blank = True, null=False)
    tel_res = models.IntegerField(verbose_name="Telefone Residêncial", blank = True, unique= True)
    celular = models.IntegerField(verbose_name="Celular/Whatsapp", blank = True, unique= True)
    formacao = models.CharField(max_length=50, verbose_name="Formação Acadêmica", blank = False, null=False)#Armazenar histórico de alterações/Separar situação[ concluído, cursando, trancado ]  ( não será incluído no sistema )/Incluir Previsão Finalização ( não será incluído no sistema )
    nivel_form = models.CharField(max_length=50, verbose_name="Nível de Formação", blank = False, null=False)
    endereco = models.CharField(max_length=100, verbose_name="Endereço", blank = True, null=False)
    uf = models.CharField(max_length=2, choices=choices_uf, verbose_name="UF", blank = True, null=False)
    municipio = models.CharField(max_length=30, verbose_name="Município", blank = True, null=False)
    bairro = models.CharField(max_length=30, verbose_name="Bairro", blank = True, null=False)
    logradouro = models.CharField(max_length=30, verbose_name="Logradouro", blank = True, null=False)
    num_end = models.CharField(max_length=20, verbose_name="Nº", blank = True, null=False)
    comp_end = models.CharField(max_length=50, verbose_name="Complemento", blank = True, null=False)
    cep_end = models.CharField(max_length= 8, verbose_name="CEP", blank = True)
    plano_sau = models.CharField(max_length=50, verbose_name="Plano de Saúde", blank = True, null=False)
    fator_rh = models.CharField(max_length=10, choices=choices_fatorRh, verbose_name="Fator Sanguíneo", blank = True, null=False)
    banco = models.CharField(max_length=5, choices=choices_banco ,verbose_name="Banco", blank = True, null=False)
    model_veic = models.CharField(max_length=30, verbose_name="Modelo do Veículo", blank = True, null=False)
    marca_veic = models.CharField(max_length=30, verbose_name="Marca do Veículo", blank = True, null=False)
    cor_veic = models.CharField(max_length=2, choices=choices_cor_veic, verbose_name="Cor do Veículo", blank = True, null=False)
    placa_veic = models.CharField(max_length=20, verbose_name="Placa do Veículo", blank = True, null=False)
    foto_pess = models.ImageField(verbose_name="Foto Pessoal", blank = True)
    obs = models.TextField(max_length=1000, verbose_name="Observações", blank = True, null=False)