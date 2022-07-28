from django.contrib import admin

# Register your models here.
from cadColab.models import Colaboradores, ColabStatus, ColabArea
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

admin.site.register(ColabStatus)
