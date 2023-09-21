from django import forms
from .models import Pais, Departamento, Municipio

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        
class DepartamentoForm(forms.ModelForm):
    pais = forms.ModelChoiceField(queryset=Pais.objects.filter(status=True))
    class Meta:
        model = Departamento
        fields = ['pais', 'nombre']
        


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nombre} (País: {obj.pais.nombre})"


class MunicipioForm(forms.ModelForm):

    departamento = CustomModelChoiceField(queryset=Departamento.objects.filter(status=True))
    class Meta:
        model = Municipio
        fields = ['departamento', 'nombre']
