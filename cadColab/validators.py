import os
from django.core.exceptions import ValidationError


def arq_pdf_img(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg', '.pmg' ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de arquivo não suportado.')



def arq_pdf(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de arquivo não suportado.')