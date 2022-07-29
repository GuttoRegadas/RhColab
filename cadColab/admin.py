from django.contrib import admin

# Register your models here.
from cadColab.models import Colaboradores, ColabStatus, ColabArea, ColabCargo, ColabVinculo, ColabEmpresa, ColabCoordenador, ColabBolsa, ColabFomacao, ColabNivelForm, Colab_Uf, ColabMunicipio
from cadColab.forms import ColaboradoresForms




@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ("nome", "status", "matricula", "area", "cargo", "ramal", "vacinado", "cpf",)
    readonly_fields = ()
    fields = ["nome", "status", "matricula", "vinculo", "area", "cargo", "ingresso", "posseFioce", "empresa", "bolsa", "coord_resp", "vigenc_bolsa", "email_pess", "adic_ocup", "ramal", "cracha", "amb_sala", "vacinado", "card_vac", "genero", "cpf", "nascimento", "rg_ident", "orgao_ident", "tel_res", "celular", "formacao", "nivel_form", "estado", "municipio", "cep_end", "bairro", "logradouro", "num_end", "comp_end", "plano_sau", "fator_rh", "banco", "model_veic", "cor_veic", "placa_veic", "foto_pess", "obs",]
    form = ColaboradoresForms
    class Media:
        js = (
            "jquery.mask.min.js",
            "custom.js",
            )
#    def save_model(self, request, obj, form, change):
#        super().save_model(request, obj, form, change)




@admin.register(ColabStatus)
class ColabStatusAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabArea)
class ColabAreaAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabCargo)
class ColabCargoAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabVinculo)
class ColabVinculoAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabEmpresa)
class ColabEmpresaAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabCoordenador)
class ColabCoordenadorAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabBolsa)
class ColabBolsaAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabFomacao)
class ColabFomacaoAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(ColabNivelForm)
class ColabNivelFormAdmin(admin.ModelAdmin):
    view_on_site = True

@admin.register(Colab_Uf)
class Colab_UfAdmin(admin.ModelAdmin):
    view_on_site = True
    list_display = ("sigla", "nome")

@admin.register(ColabMunicipio)
class ColabMunicipioAdmin(admin.ModelAdmin):
    view_on_site = True
    list_display = ("uf", "municipio")