from django.db import models
import os
from .validators import arq_pdf_img, arq_pdf
# Create your models here.

class ColabStatus(models.Model):
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    colabStatus = models.CharField(max_length=50, verbose_name="Descrição do Status", blank=True, null=True)
    def __str__(self):
        return f'{self.colabStatus}'

class ColabArea(models.Model):
    colabArea = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabCargo(models.Model):

    colabCargo = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabVinculo(models.Model):

    colabVinculo = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabEmpresa(models.Model):

    colabEmpresa = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabCoordenador(models.Model):

    colabCoord = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabBolsa(models.Model):

    colabBolsa = models.CharField(max_length=50, verbose_name="Descrição do Vínculo", blank=True, null=True)

class ColabFomacao(models.Model):

    colabFomacao = models.CharField(max_length=100, verbose_name="Formação", blank=True, null=True)

class ColabNivelForm(models.Model):

    colabNivelForm = models.CharField(max_length=100, verbose_name="Nível de Formação", blank=True, null=True)

class Colab_Uf(models.Model):

    nome = models.CharField(max_length=50, verbose_name="Nome do Estado", blank=True, null=True)
    sigla = models.CharField(max_length=6, verbose_name="Sigla do Estado", blank=True, null=True)
    

class ColabMunicipio(models.Model):

    uf = models.ForeignKey(Colab_Uf, on_delete= models.RESTRICT, verbose_name="UF", null=True)
    municipio = models.CharField(max_length=100, verbose_name="Município", blank=True, null=True)



class Colaboradores(models.Model):

    class Meta:
        verbose_name = "Colaboradores"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return f'{self.nome}'
    
#Dados Funcionais------------------------------------------------------------------------------------------------------------------------------------------------------

    nome = models.CharField(max_length=50, verbose_name="Colaborador", blank = False)

#Campo Choices/Extrair o vínculo da planilha/campo obrigatória
    status = models.ForeignKey(ColabStatus, on_delete= models.RESTRICT, blank = False, null=True)

#Extrair o vínculo da planilha/campo obrigatória
    vinculo = models.ForeignKey(ColabVinculo, on_delete= models.RESTRICT, blank = False, null=True)

#Lista extraída da planilha,/Obrigatório se vínculo = Servidor
    cargo = models.ForeignKey(ColabCargo, on_delete= models.RESTRICT, blank = False, null=True)

#se vínculo = servidor é obrigatório
    matricula = models.CharField(max_length=20, verbose_name= "Mátricula", blank = False, unique= True)

#lista obtida no organograma do SGA
    area = models.ForeignKey(ColabArea, on_delete= models.RESTRICT, blank = False, null=True)
    
    ingresso = models.DateField(verbose_name="Data do Ingresso", blank = True)
    posseFioce = models.DateField(verbose_name="Data da Posse", blank = True)
    
#Lista extraída da planilha/Obrigatório se vínculo = Terceirizado
#Obs: Armazenar histórico de alterações
    empresa = models.ForeignKey(ColabEmpresa, on_delete= models.RESTRICT, blank = False, null=True)

#Lista extraída da planilha/Obrigatório se vínculo = Bolsista
    bolsa = models.ForeignKey(ColabBolsa, on_delete=models.RESTRICT, blank = False, null=True)

#Lista [ RH ], opcional
    coord_resp = models.ForeignKey(ColabCoordenador, on_delete=models.RESTRICT, blank = True, null=True)

#Solicitado apenas para Bolsista
    vigenc_bolsa = models.DateField(verbose_name="Data Vigência" , blank = True)

    email_pess = models.EmailField(verbose_name="E-mail Pessoal" , blank = True, unique= True)
    adic_ocup = models.BooleanField(verbose_name="Adic. Ocupacional", blank = True)
    ramal = models.CharField(max_length=12, verbose_name="Ramal", blank = True)
    cracha = models.CharField(max_length=30, verbose_name="Crachá", blank = True)
    amb_sala = models.CharField(max_length=30, verbose_name="Sala", blank = True)#Lista de Salas obtida no Controle de Claviculário
    vacinado = models.BooleanField(verbose_name="Vacinação", blank = True)
    card_vac = models.FileField(max_length=255, upload_to = 'Cartão de Vacina', verbose_name="Comprovante de Vacina", blank = True, null=True, validators=[arq_pdf_img])


#Dados Pessoais---------------------------------------------------------------------------------------------------------------------------------------------------------
    choices_genero = (
        ("MC", "Mulher cisgênera"),
        ("MT", "Mulher trans"),
        ("HC", "Homem cisgênero"),
        ("HT", "Homem trans"),
        ("NB", "Pessoa não-binária"),
        ("NL", "Nenhuma das opções listadas"),
        ("NR", "Prefiro não responder"),
        )
    genero = models.CharField(max_length=2, choices=choices_genero, verbose_name="Identidade de Gênero", blank = True)

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
    fator_rh = models.CharField(max_length=10, choices=choices_fatorRh, verbose_name="Fator Sanguíneo", blank = True)

    cpf = models.CharField(max_length=11, verbose_name="CPF", blank = False, unique= True)
    nascimento = models.DateField(verbose_name="Data Nascimento", blank = False)
    rg_ident = models.IntegerField(verbose_name="Identidade", blank = True)
    orgao_ident = models.CharField(max_length=20, verbose_name="Orgão Espedidor", blank = True)
    tel_res = models.CharField(max_length=25,verbose_name="Telefone Residêncial", blank = True)
    celular = models.CharField(max_length=25,verbose_name="Celular/Whatsapp", blank = True)

#Armazenar histórico de alterações/Separar situação[ concluído, cursando, trancado ]  ( não será incluído no sistema )/Incluir Previsão Finalização ( não será incluído no sistema )
    formacao = models.CharField(max_length=50, verbose_name="Formação Acadêmica", blank = False)

    nivel_form = models.ForeignKey(ColabNivelForm, verbose_name="Nível de Formação", on_delete=models.RESTRICT, blank = False, null=True)
    estado = models.ForeignKey(Colab_Uf, verbose_name="Estado", on_delete=models.RESTRICT, blank = False, null=True)
    municipio = models.ForeignKey(ColabMunicipio, verbose_name = "Município", on_delete=models.RESTRICT, blank = False, null=True)
    bairro = models.CharField(max_length=30, verbose_name="Bairro", blank = True)
    logradouro = models.CharField(max_length=30, verbose_name="Logradouro", blank = False)
    num_end = models.CharField(max_length=20, verbose_name="Nº", blank = True)
    comp_end = models.CharField(max_length=50, verbose_name="Complemento", blank = True)
    cep_end = models.CharField(max_length= 20, verbose_name="CEP", blank = True)
    plano_sau = models.CharField(max_length=50, verbose_name="Plano de Saúde", blank = True)
    banco = models.CharField(max_length=100, verbose_name="Banco", blank = True)
    model_veic = models.CharField(max_length=30, verbose_name="Modelo do Veículo", blank = True)
    marca_veic = models.CharField(max_length=30, verbose_name="Marca do Veículo", blank = True)

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
    cor_veic = models.CharField(max_length=2, choices=choices_cor_veic, verbose_name="Cor do Veículo", blank = True)
    placa_veic = models.CharField(max_length=20, verbose_name="Placa do Veículo", blank = True)
    foto_pess = models.FileField(max_length=255, upload_to="Foto", verbose_name="Foto Pessoal", blank = True, validators=[arq_pdf_img])
    obs = models.TextField(max_length=1000, verbose_name="Observações", blank = True)


# UpLoad do cartão de vacinação "card_vac"----------------------------------------------------------------------------
    def delete(self, using=None, keep_parents=False):
        if self.card_vac.name:
            self.card_vac.storage.delete(self.card_vac.name)
        super().delete()

    def __init__(self, *args, **kwargs):
        super( Colaboradores, self).__init__(*args, **kwargs)
        setattr(self, '__original_card_vac', getattr(self, 'card_vac'))
        
    def save( self, *args, **kwargs ):
        fd_ant = getattr(self, '__original_card_vac') 
        if fd_ant:
            fd_ant = fd_ant.path
            fd_new = getattr(self, 'card_vac')
            if fd_ant != fd_new:
                if os.path.exists( fd_ant ):
                    os.remove( fd_ant )
#---------------------------------------------------------------------------------------------------------------------

# UpLoad do foto pessoal "foto_pess"----------------------------------------------------------------------------------

    def delete(self, using=None, keep_parents=False):
        if self.foto_pess.name:
            self.foto_pess.storage.delete(self.foto_pess.name)
        super().delete()

    def __init__(self, *args, **kwargs):
        super( Colaboradores, self).__init__(*args, **kwargs)
        setattr(self, '__original_foto_pess', getattr(self, 'foto_pess'))
        
    def save( self, *args, **kwargs ):
        fd_ant = getattr(self, '__original_foto_pess') 
        if fd_ant:
            fd_ant = fd_ant.path
            fd_new = getattr(self, 'foto_pess')
            if fd_ant != fd_new:
                if os.path.exists( fd_ant ):
                    os.remove( fd_ant )
#---------------------------------------------------------------------------------------------------------------------