from django import forms
from .models import Pledge

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'organs_to_donate': forms.Textarea(attrs={'rows': 3}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }
