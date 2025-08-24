from django import forms
from .models import Pledge

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['name', 'email', 'phone', 'age', 'city', 'organs', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Your Age'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'organs': forms.Select(),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message (Optional)', 'rows': 3}),
        }
