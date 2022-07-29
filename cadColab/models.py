from django.db import models
import os

from django.dispatch import receiver
from .validators import arq_pdf_img, arq_pdf
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import pre_save

class ColabStatus(models.Model):
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    colabStatus = models.CharField(max_length=50, verbose_name="Descrição do Status")
    def __str__(self):
        return f'{self.colabStatus}'

class ColabArea(models.Model):
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    colabArea = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabArea}'

class ColabCargo(models.Model):
    class Meta:
        verbose_name = "Lista de Cargo"
        verbose_name_plural = "Listas de Cargos"

    colabCargo = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabCargo}'
        
class ColabVinculo(models.Model):
    class Meta:
        verbose_name = "Vínculo"
        verbose_name_plural = "Vinculos"

    colabVinculo = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabVinculo}'

class ColabEmpresa(models.Model):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    colabEmpresa = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabEmpresa}'

class ColabCoordenador(models.Model):
    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    colabCoord = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabCoord}'

class ColabBolsa(models.Model):
    class Meta:
        verbose_name = "Bolsa"
        verbose_name_plural = "Bolsas"

    colabBolsa = models.CharField(max_length=50, verbose_name="Descrição do Vínculo")
    def __str__(self):
        return f'{self.colabBolsa}'

class ColabFomacao(models.Model):
    class Meta:
        verbose_name = "Formacão"
        verbose_name_plural = "Formações"

    colabFomacao = models.CharField(max_length=100, verbose_name="Formação")
    def __str__(self):
        return f'{self.colabFomacao}'

class ColabNivelForm(models.Model):
    class Meta:
        verbose_name = "Nível de Formação"
        verbose_name_plural = "Níveis de Formação"

    colabNivelForm = models.CharField(max_length=100, verbose_name="Nível de Formação")
    def __str__(self):
        return f'{self.colabNivelForm}'

class Colab_Uf(models.Model):
    class Meta:
        verbose_name = "UF - Estado"
        verbose_name_plural = "UF's - Estados"
        
    nome = models.CharField(max_length=50, verbose_name="Nome do Estado")
    sigla = models.CharField(max_length=6, verbose_name="Sigla do Estado")
    def __str__(self):
        return f'{self.nome}'

class ColabMunicipio(models.Model):
    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"

    uf = models.ForeignKey(Colab_Uf, on_delete= models.PROTECT, verbose_name="UF")
    municipio = models.CharField(max_length=100, verbose_name="Município")
    def __str__(self):
        return f'{self.municipio}'

#Tabela de Cadastro de Colaboradores------------------------------------------------------------------------------------------------------------------------------------------------------
class Colaboradores(models.Model):

    class Meta:
        verbose_name = "Cadastro de Colaboradores"
        verbose_name_plural = "Cadastro de Colaboradores"
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome

    
#Dados Funcionais------------------------------------------------------------------------------------------------------------------------------------------------------

    #id = models.IntegerField( primary_key=True )
    nome = models.CharField(max_length=50, verbose_name="Colaborador")

    status = models.ForeignKey(ColabStatus, on_delete= models.PROTECT)#Campo Choices/Extrair o vínculo da planilha/campo obrigatória

    vinculo = models.ForeignKey(ColabVinculo, on_delete= models.PROTECT)#Extrair o vínculo da planilha/campo obrigatória

    cargo = models.ForeignKey(ColabCargo, on_delete= models.PROTECT)#Lista extraída da planilha,/Obrigatório se vínculo = Servidor

    matricula = models.CharField(max_length=20, verbose_name= "Mátricula", unique= True)#se vínculo = servidor é obrigatório

    area = models.ForeignKey(ColabArea, on_delete= models.PROTECT)#lista obtida no organograma do SGA
    
    ingresso = models.DateField(verbose_name="Data do Ingresso", blank = True, null=True)
    posseFioce = models.DateField(verbose_name="Data da Posse", blank = True, null=True)
    
    empresa = models.ForeignKey(ColabEmpresa, on_delete= models.PROTECT)#Lista extraída da planilha/Obrigatório se vínculo = Terceirizado
#Obs: Armazenar histórico de alterações

    bolsa = models.ForeignKey(ColabBolsa, on_delete=models.PROTECT)#Lista extraída da planilha/Obrigatório se vínculo = Bolsista

    coord_resp = models.ForeignKey(ColabCoordenador, on_delete=models.PROTECT)#Lista [ RH ], opcional

    vigenc_bolsa = models.DateField(verbose_name="Data Vigência" , blank = True, null=True)#Solicitado apenas para Bolsista

    email_pess = models.EmailField(verbose_name="E-mail Pessoal" , blank = True, null=True)
    adic_ocup = models.BooleanField(verbose_name="Adic. Ocupacional", blank = True, null=True)
    ramal = models.CharField(max_length=12, verbose_name="Ramal", blank = True, null=True)
    cracha = models.CharField(max_length=30, verbose_name="Crachá", blank = True, null=True)
    amb_sala = models.CharField(max_length=30, verbose_name="Sala", blank = True, null=True)#Lista de Salas obtida no Controle de Claviculário
    vacinado = models.BooleanField(verbose_name="Vacinação", blank = True, null=True)
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
    genero = models.CharField(max_length=2, choices=choices_genero, verbose_name="Identidade de Gênero", blank = True, null=True)

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
    fator_rh = models.CharField(max_length=10, choices=choices_fatorRh, verbose_name="Fator Sanguíneo", blank = True, null=True)

    cpf = models.CharField(max_length=14, verbose_name="CPF", blank = False, unique= True)
    nascimento = models.DateField(verbose_name="Data Nascimento")
    rg_ident = models.CharField(max_length=25, verbose_name="Identidade", blank = True, null=True)
    orgao_ident = models.CharField(max_length=20, verbose_name="Orgão Espedidor", blank = True, null=True)
    tel_res = models.CharField(max_length=25,verbose_name="Telefone Residêncial", blank = True, null=True)
    celular = models.CharField(max_length=25,verbose_name="Celular/Whatsapp", blank = True, null=True)

    formacao = models.ForeignKey(ColabFomacao, on_delete=models.PROTECT, verbose_name="Formação Acadêmica", blank = False, null=False)#Armazenar histórico de alterações/Separar situação[ concluído, cursando, trancado ]  ( não será incluído no sistema )/Incluir Previsão Finalização ( não será incluído no sistema )

    nivel_form = models.ForeignKey(ColabNivelForm, verbose_name="Nível de Formação", on_delete=models.PROTECT)
    estado = models.ForeignKey(Colab_Uf, verbose_name="Estado", on_delete=models.PROTECT)
    municipio = models.ForeignKey(ColabMunicipio, verbose_name = "Município", on_delete=models.PROTECT)
    bairro = models.CharField(max_length=30, verbose_name="Bairro", blank = True, null=True)
    logradouro = models.CharField(max_length=30, verbose_name="Logradouro")
    num_end = models.CharField(max_length=20, verbose_name="Nº", blank = True, null=True)
    comp_end = models.CharField(max_length=50, verbose_name="Complemento", blank = True, null=True)
    cep_end = models.CharField(max_length= 20, verbose_name="CEP", blank = True, null=True)
    plano_sau = models.CharField(max_length=50, verbose_name="Plano de Saúde", blank = True, null=True)
    banco = models.CharField(max_length=100, verbose_name="Banco", blank = True, null=True)
    model_veic = models.CharField(max_length=30, verbose_name="Modelo do Veículo", blank = True, null=True)
    marca_veic = models.CharField(max_length=30, verbose_name="Marca do Veículo", blank = True, null=True)

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
    cor_veic = models.CharField(max_length=2, choices=choices_cor_veic, verbose_name="Cor do Veículo", blank = True, null=True)
    placa_veic = models.CharField(max_length=20, verbose_name="Placa do Veículo", blank = True, null=True)
    foto_pess = models.FileField(max_length=255, upload_to="Foto", verbose_name="Foto Pessoal", blank = True, validators=[arq_pdf_img], null=True)
    obs = models.TextField(max_length=1000, verbose_name="Observações", blank = True, null=True)


# UpLoad do cartão de vacinação "card_vac"----------------------------------------------------------------------------
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

        # Chamando o save padrão.
        super( Colaboradores, self ).save( *args, **kwargs )

 
@receiver( pre_save, sender = Colaboradores )
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        print('Entrou Ficha pre_save')
        old_arq = instance.__class__.objects.get( id = instance.id ).foto_pess.path
        print( f"old_arq { old_arq }" )
        try:
            new_arq = instance.foto_pess.path
            print( f"new_arq { new_arq }" )
        except:
            new_arq = None
            print( f"new_arq except{ new_arq }" )
        if new_arq != old_arq:
            print( f"new_arq:{ new_arq } != old_arq:{ old_arq }" )
            if os.path.exists( old_arq ):
                print( "os.path.exists( old_arq )" )
                os.remove( old_arq )
    except:
        pass

#---------------------------------------------------------------------------------------------------------------------

# UpLoad do foto pessoal "foto_pess"----------------------------------------------------------------------------------

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

        # Chamando o save padrão.
        super( Colaboradores, self ).save( *args, **kwargs )

 
@receiver( pre_save, sender = Colaboradores )
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        print('Entrou Ficha pre_save')
        old_arq = instance.__class__.objects.get( id = instance.id ).foto_pess.path
        print( f"old_arq { old_arq }" )
        try:
            new_arq = instance.foto_pess.path
            print( f"new_arq { new_arq }" )
        except:
            new_arq = None
            print( f"new_arq except{ new_arq }" )
        if new_arq != old_arq:
            print( f"new_arq:{ new_arq } != old_arq:{ old_arq }" )
            if os.path.exists( old_arq ):
                print( "os.path.exists( old_arq )" )
                os.remove( old_arq )
    except:
        pass
#---------------------------------------------------------------------------------------------------------------------