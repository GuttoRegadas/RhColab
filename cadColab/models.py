from django.db import models

# Create your models here.

class ColabStatus(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição do Status", blank = False, null=False)

class ColabArea(models.Model):
    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)

class ColabCargo(models.Model):

    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)

class ColabVinculo(models.Model):

    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)

class ColabEmpresa(models.Model):

    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)

class ColabCoordenador(models.Model):

    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)

class ColabBolsa(models.Model):

    descricao =models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank = False, null = False)



class Colaboradores(models.Model):
    
#Dados Funcionais------------------------------------------------------------------------------------------------------------------------------------------------------

    nome = models.CharField(max_length=50, verbose_name="Colaborador", blank = False, null=False)

    #status = models.CharField(max_length=1, verbose_name= "Status", blank = False, null=False)#Campo Choices/Extrair o vínculo da planilha/campo obrigatória
    status = models.ForeignKey(ColabStatus, on_delete= models.RESTRICT)

    matricula = models.IntegerField(verbose_name= "Mátricula", blank = False, null=False, unique= True)#se vínculo = servidor é obrigatório

    #vinculo = models.CharField(max_length=20, verbose_name="Vínculo", blank = False, null=False)#Extrair o vínculo da planilha/campo obrigatória
    vinculo = models.ForeignKey(ColabVinculo, on_delete= models.RESTRICT)

    #area = models.CharField(max_length=20, verbose_name="Área", blank = False, null=False)#lista obtida no organograma do SGA
    area = models.ForeignKey(ColabArea, on_delete= models.RESTRICT)

    #cargo = models.CharField(max_length=30, verbose_name="Cargo", blank = False, null=False)#Lista extraída da planilha,/Obrigatório se vínculo = Servidor
    cargo = models.ForeignKey(ColabCargo, on_delete= models.RESTRICT)
    
    ingresso = models.DateField(verbose_name="Data do Ingresso", blank = True)
    posseFioce = models.DateField(verbose_name="Data da Posse", blank = True)
    
    #empresa = models.CharField(max_length=50, verbose_name="Empresa", blank = False, null=False)#Lista extraída da planilha/Obrigatório se vínculo = Terceirizado
    empresa = models.ForeignKey(ColabEmpresa, on_delete= models.RESTRICT)

#Obs: Armazenar histórico de alterações

    #bolsa = models.CharField(max_length=1, verbose_name="Bolsa", blank = False, null=False)#Lista extraída da planilha/Obrigatório se vínculo = Bolsista
    bolsa = models.ForeignKey(ColabBolsa, on_delete=models.RESTRICT)

    #coord_resp = models.CharField(max_length=30, verbose_name="Coordenador Responsável", blank = True, null=False)#Lista [ RH ], opcional
    coord_resp = models.ForeignKey(ColabCoordenador, on_delete=models.CASCADE)

    vigenc_bolsa = models.DateField(verbose_name="Data Vigência" , blank = True)#Solicitado apenas para Bolsista
    email_pess = models.EmailField(verbose_name="E-mail Pessoal" , blank = True, unique= True)
    adic_ocup = models.BooleanField(verbose_name="Adic. Ocupacional", blank = True)
    ramal = models.IntegerField(verbose_name="Ramal", blank = True)
    cracha = models.CharField(max_length=30, verbose_name="Crachá", blank = True, null=False, unique= True)
    amb_sala = models.CharField(max_length=30, verbose_name="Sala", blank = True, null=False)#Lista de Salas obtida no Controle de Claviculário
    vacinado = models.BooleanField(verbose_name="Vaciando", blank = True)
    card_vac = models.CharField(max_length=255, verbose_name="Comprovante de Vacina", blank = True)


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
    rg_ident = models.IntegerField(verbose_name="Identidade")
    orgao_ident = models.CharField(max_length=20, verbose_name="Orgão Espedidor", blank = True, null=False)
    tel_res = models.CharField(max_length=25,verbose_name="Telefone Residêncial", blank = True, unique= True)
    celular = models.CharField(max_length=25,verbose_name="Celular/Whatsapp", blank = True, unique= True)
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
    banco = models.CharField(max_length=100, verbose_name="Banco", blank = True, null=False)
    model_veic = models.CharField(max_length=30, verbose_name="Modelo do Veículo", blank = True, null=False)
    marca_veic = models.CharField(max_length=30, verbose_name="Marca do Veículo", blank = True, null=False)
    cor_veic = models.CharField(max_length=2, choices=choices_cor_veic, verbose_name="Cor do Veículo", blank = True, null=False)
    placa_veic = models.CharField(max_length=20, verbose_name="Placa do Veículo", blank = True, null=False)
    foto_pess = models.CharField(max_length=255, verbose_name="Foto Pessoal", blank = True)
    obs = models.TextField(max_length=1000, verbose_name="Observações", blank = True, null=False)