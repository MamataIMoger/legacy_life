# eligibility/utils.py

def evaluate_eligibility(data):
    age = data.get('age')
    bmi = data.get('bmi')
    chronic_disease = data.get('chronic_disease')
    infection = data.get('infection')

    if age < 18 or age > 65:
        return (
            "Not Eligible",
            "Your age is outside the acceptable range (18–65).",
            "You can consider tissue donation or encourage others to donate."
        )

    if chronic_disease:
        return (
            "Not Eligible",
            "You have a major chronic disease.",
            "Speak to a doctor about managing your condition. You can still pledge."
        )

    if infection:
        return (
            "Not Eligible",
            "You have an active infection.",
            "Wait until you're fully recovered and try again."
        )

    if bmi < 18.5 or bmi > 30:
        return (
            "Not Eligible",
            "Your BMI is outside the healthy range (18.5–30).",
            "Try to reach a healthy BMI and consult a doctor."
        )

    return ("Eligible", "", "")
