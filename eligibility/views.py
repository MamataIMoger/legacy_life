from django.shortcuts import render
from .forms import EligibilityForm
from .models import EligibilityCheck

def check_eligibility(request):
    result = None
    hospitals = []

    if request.method == 'POST':
        form = EligibilityForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            bmi = form.cleaned_data['bmi']
            chronic = form.cleaned_data['chronic_disease']
            infection = form.cleaned_data['infection']

            if 18 <= age <= 65 and 18.5 <= bmi <= 30 and not chronic and not infection:
                is_eligible = True
                result = 'Eligible'
                hospitals = ['Apollo Hospital', 'Fortis Health', 'AIIMS', 'Manipal Hospital']
            else:
                is_eligible = False
                result = 'Not Eligible'

            # Save the check to the database
            EligibilityCheck.objects.create(
                age=age,
                bmi=bmi,
                chronic_disease=chronic,
                infection=infection,
                is_eligible=is_eligible
            )
    else:
        form = EligibilityForm()

    return render(request, 'check.html', {
        'form': form,
        'result': result,
        'hospitals': hospitals
    })
