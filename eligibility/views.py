from django.shortcuts import render
from .forms import EligibilityForm
from .models import EligibilityCheck
from .utils import evaluate_eligibility  

def check_eligibility(request):
    result = None
    hospitals = []
    ineligibility_reason = ""
    advice = ""

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
                hospitals = [
                    {"name": "Apollo Hospital", "location": "Bangalore", "website": "https://www.apollohospitals.com"},
                    {"name": "Fortis Health", "location": "Mumbai", "website": "https://www.fortishealthcare.com"},
                    {"name": "AIIMS", "location": "Delhi", "website": "https://www.aiims.edu"},
                    {"name": "Manipal Hospital", "location": "Hyderabad", "website": "https://www.manipalhospitals.com"},
                ]
            else:
                is_eligible = False
                result = 'Not Eligible'

                # Identify reason and give advice
                if age < 18 or age > 65:
                    ineligibility_reason = "Your age is not in the eligible range (18–65)."
                    advice = "You can still support organ donation by encouraging others or registering as a tissue donor."
                elif bmi < 18.5 or bmi > 30:
                    ineligibility_reason = "Your BMI is outside the healthy donation range (18.5–30)."
                    advice = "Try to achieve a healthier BMI and consult your doctor for further evaluation."
                elif chronic:
                    ineligibility_reason = "You have a major chronic disease."
                    advice = "Organ donation might not be possible now, but you can still pledge your eyes or tissues."
                elif infection:
                    ineligibility_reason = "You have an active infection."
                    advice = "Once the infection is treated and cleared, you can re-check eligibility."

            # Save record
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
        'hospitals': hospitals,
        'ineligibility_reason': ineligibility_reason,
        'advice': advice
    })
