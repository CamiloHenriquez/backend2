from django import forms
from Funcion.models import Funcion

class registroFunciones(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = '__all__'