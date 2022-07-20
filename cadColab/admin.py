from django.contrib import admin

# Register your models here.
from .models import Colaboradores

@admin.register(Colaboradores)
class ColaboraresAdmin(admin.ModelAdmin):
    list_display = ("nome", "status", "matricula", "area", "cargo", "ramal", "vacinado", "cpf",)
    readonly_fields = ()
    fields = ["nome", "status", "matricula", "vinculo", "area", "cargo", "ingresso", "posseFioce", "empresa", "bolsa", "coord_resp", "vigenc_bolsa", "email_pess", "adic_ocup", "ramal", "cracha", "amb_sala", "vacinado", "card_vac", "genero", "cpf", "nascimento", "identidade", "orgao_ident", "tel_res", "celular", "formacao", "nivel_form", "endereco", "uf", "municipio", "bairro", "logradouro", "num_end", "comp_end", "plano_sau", "fator_rh", "banco", "obs", "model_veic", "cor_veic", "placa_veic", "foto_pess", ]
