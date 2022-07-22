from django import forms


class ColaboradoresFormsAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ColaboradoresFormsAdmin, self). __init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['celular'].widget.attrs['class'] = 'mask-celular'
        self.fields['cep_end'].widget.attrs['class'] = 'mask-cep'