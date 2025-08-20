from django.shortcuts import render, redirect
from .forms import PledgeForm

def pledge_form(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save()  # save and keep the object
            # ✅ Render the thank you page and pass pledge.full_name
            return render(request, 'pledge_thank_you.html', {"name": pledge.full_name})
    else:
        form = PledgeForm()
    # ✅ make sure template path has pledges/ since it's inside pledges/templates/pledges/
    return render(request, 'pledge_form.html', {'form': form})
