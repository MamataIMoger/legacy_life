from django.shortcuts import render

def simulator_home(request):
    if request.method == 'POST':
        increase = int(request.POST.get('increase', 0))
        lives_saved = increase * 30  # example logic
        return render(request, 'simulator_result.html', {
            'increase': increase,
            'lives_saved': lives_saved
        })
    return render(request, 'simulator.html')

def simulator_result(request):
    return render(request, 'simulator_result.html')
