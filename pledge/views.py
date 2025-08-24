from django.shortcuts import render
from .forms import PledgeForm

def make_pledge(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            pledge = form.save()
            return render(request, 'pledge_thank_you.html', {'name': pledge.name})
    else:
        form = PledgeForm()

    return render(request, 'pledge_form.html', {'form': form})
