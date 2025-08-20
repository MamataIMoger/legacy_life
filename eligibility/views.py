from django.shortcuts import render
from .models import Hospital

def check_eligibility(request):
    hospitals = None
    result = None
    eligible = False

    if request.method == "POST":
        try:
            # Collect form inputs
            age = int(request.POST.get("age"))
            chronic_disease = request.POST.get("chronic_disease") == "yes"
            infection = request.POST.get("infection") == "yes"
            recent_surgery = request.POST.get("recent_surgery") == "yes"
            cancer_history = request.POST.get("cancer_history") == "yes"
            organ = request.POST.get("organ")   # Kidney, Eye, Heart, Liver

            # Eligibility logic
            if not (18 <= age <= 65):
                result = "Age must be between 18 and 65."
            elif chronic_disease:
                result = "You have a chronic disease, which makes you ineligible."
            elif infection:
                result = "You have an active infection, which makes you ineligible."
            elif recent_surgery:
                result = "You recently had a major surgery, hence ineligible."
            elif cancer_history:
                result = "History of cancer makes you ineligible for donation."
            else:
                eligible = True
                result = f"Congratulations! You are eligible to donate your {organ}."
                hospitals = Hospital.objects.all()

        except (TypeError, ValueError):
            result = "Invalid input. Please enter correct values."

    return render(
        request,
        "check.html",
        {"result": result, "hospitals": hospitals, "eligible": eligible}
    )
