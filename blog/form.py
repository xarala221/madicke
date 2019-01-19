
from django import forms

from .models import Superviser

class ConfigurationForm(forms.ModelForm):

    class Meta:
        model = Superviser

        

        fields = ('equipement', 'types','description')

        widgets = {
            'types': forms.TextInput(attrs={'placeholder': 'Entrer votre type d"equipement '}),
            'description': forms.Textarea(attrs={'placeholder': 'Entrer la description de la configuration de votre equipement'}),
        }