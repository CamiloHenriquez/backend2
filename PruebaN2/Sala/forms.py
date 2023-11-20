from django import forms
from Sala.models import Sala

class registroSalas(forms.ModelForm):
    class Meta:
        model=Sala
        fields='__all__'