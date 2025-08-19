from django.shortcuts import render
from .models import Hospital

def check_eligibility(request):
    hospitals = None
    result = None

    if request.method == "POST":
        try:
            age = int(request.POST.get("age"))
            bmi = float(request.POST.get("bmi"))
        except (TypeError, ValueError):
            result = "Invalid input. Please enter correct values."
            return render(request, "check.html", {"result": result, "hospitals": hospitals})

        chronic_disease = request.POST.get("chronic_disease") == "yes"
        infection = request.POST.get("infection") == "yes"
        recent_surgery = request.POST.get("recent_surgery") == "yes"
        cancer_history = request.POST.get("cancer_history") == "yes"
        substance_abuse = request.POST.get("substance_abuse") == "yes"
        pregnant = request.POST.get("pregnant") == "yes"

        is_eligible = (
            18 <= age <= 65 and
            18.5 <= bmi <= 24.9 and
            not chronic_disease and
            not infection and
            not recent_surgery and
            not cancer_history and
            not substance_abuse and
            not pregnant
        )

        if is_eligible:
            result = "Congratulations! You are eligible for organ donation."
            hospitals = Hospital.objects.all()
        else:
            result = "Sorry, you are not eligible for organ donation."

    return render(request, "check.html", {"result": result, "hospitals": hospitals})
