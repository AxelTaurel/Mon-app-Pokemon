from django import forms
 
from .models import carte
 

class cartePvForm(forms.ModelForm):
    class Meta:
        model = carte
        fields = ['Pv']  # Limitez aux PV uniquement

