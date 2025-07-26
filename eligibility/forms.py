from django import forms

class EligibilityForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    age = forms.IntegerField(label='Age')
    bmi = forms.FloatField(label='BMI')
    chronic_disease = forms.BooleanField(label='Any chronic disease?', required=False)
    infection = forms.BooleanField(label='Active infection?', required=False)
    organ_donor_before = forms.BooleanField(label='Have you donated before?', required=False)
    recent_surgery = forms.BooleanField(required=False)
    cancer_history = forms.BooleanField(required=False)
    substance_abuse = forms.BooleanField(required=False)
    pregnant = forms.BooleanField(required=False)  # for female users
