from django import forms
from .models import Pais, Departamento, Municipio

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['pais', 'nombre']
        
class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['departamento', 'nombre']
