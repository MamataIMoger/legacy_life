from django import forms
from .models import Hospital

class EligibilityForm(forms.Form):
    age = forms.IntegerField(label="Age")
    bmi = forms.FloatField(label="BMI")
    chronic_disease = forms.BooleanField(required=False, label="Any chronic diseases?")
    infection = forms.BooleanField(required=False, label="Any active infections?")
    recent_surgery = forms.BooleanField(required=False, label="Had recent surgery?")
    cancer_history = forms.BooleanField(required=False, label="Any history of cancer?")
    substance_abuse = forms.BooleanField(required=False, label="History of substance abuse?")
    pregnant = forms.BooleanField(required=False, label="Currently pregnant?")

    # New Multiple Choice Field
    TRANSPLANT_CHOICES = [
        ('kidney', 'Kidney'),
        ('liver', 'Liver'),
        ('heart', 'Heart'),
        ('lungs', 'Lungs'),
        ('pancreas', 'Pancreas'),
        ('cornea', 'Cornea'),
    ]
    organ_choice = forms.ChoiceField(
        choices=TRANSPLANT_CHOICES,
        widget=forms.RadioSelect,
        label="Which type of organ transplant are you considering?"
    )

    # New Open Text Field
    thoughts = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your thoughts on organ donation...'}),
        required=False,
        label="Your thoughts on organ donation"
    )


class HospitalSelectionForm(forms.Form):
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        widget=forms.RadioSelect,
        label="Select a hospital"
    )
