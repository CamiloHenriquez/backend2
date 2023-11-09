from django import forms
from Cine.models import Cine

class registroCines(forms.ModelForm):
    class Meta:
        model = Cine
        fields = '__all__'
    