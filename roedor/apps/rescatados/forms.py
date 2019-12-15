from django import forms
from .models import Adoptante, Mascota, Ficha

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['run', 'nombre', 'apellido', 'direccion', 'ciudad', 'telefono', 'correo']


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombreM', 'tipo_roedor', 'ciudadM', 'infoM']    

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields =['run_adop','fecha','mascota_adop']

        