from django.shortcuts import render

def myths(request):
    myths_data = [
        {"myth": "Organ donation disfigures the body.",
         "fact": "Organs are removed with surgical precision, and the body is respectfully restored."},
        {"myth": "I am too old to donate organs.",
         "fact": "Organs are accepted based on health and not age."},
        {"myth": "Doctors won't try to save me if I'm an organ donor.",
         "fact": "Doctors always prioritize saving your life first."},
        {"myth": "My religion does not allow organ donation.",
         "fact": "Most major religions support organ donation as a noble act."},
        {"myth": "Organ donation is only for the rich.",
         "fact": "Organs are allocated based on medical need, not wealth."},
        {"myth": "It costs money to become a donor.",
         "fact": "There is no cost to the donor or their family."},
        {"myth": "My body will be misused after donation.",
         "fact": "Strict laws prevent illegal organ use in India."},
        {"myth": "Only major organs like heart and kidney can be donated.",
         "fact": "Tissues like corneas, skin, bones can also be donated."},
        {"myth": "Only men can donate organs.",
         "fact": "Everyone, regardless of gender, can donate organs."},
        {"myth": "You need a donor card to donate.",
         "fact": "It's optional. Consent and family support matter more."},
        # You can add more from the full list...
    ]
    return render(request, 'myths.html', {'myths': myths_data})
