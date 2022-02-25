from django import forms
from django.forms import BaseFormSet, formset_factory


class BaseFilhosFormSet(BaseFormSet):

    # def clean_data_nascimento_filho(self):
    #     return self.cleaned_data['data_nascimento_filho']
    
    # def clean_nome_filho(self):
    #     return self.cleaned_data['nome_filho']
    
    def clean(self):
        return self.cleaned_data



class FilhoForm(forms.Form):
    nome_filho = forms.CharField(
        label="Filho(a)",
        label_suffix='',
        required=False,
    )

    data_nascimento_filho = forms.DateField(
        label="Data de nascimento do(a) filho(a)",
        label_suffix='',
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )


FilhoFormSet = formset_factory(FilhoForm, extra=5)
# FilhoFormSet = formset_factory(FilhoForm, formset=BaseFilhosFormSet, extra=5)





class RegistoForm(forms.Form):

    nome = forms.CharField(
        label="Nome",
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'nome',
            }
        )
    )

    sexo = forms.ChoiceField(
        label="Sexo",
        label_suffix='',
        choices=[
            (None, ''),
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        )
    )

    formFilhos = FilhoFormSet()