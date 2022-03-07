from django import forms
from .models import Computed_Molecular_Weight


class MWForm(forms.ModelForm):
    class Meta:
        model = Computed_Molecular_Weight
        fields = ('inchikey', 'molecular_formula',)
