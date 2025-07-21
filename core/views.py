from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Home Page View
def home(request):
    return render(request, 'home.html')

# Admin Login View
def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')
        else:
            error = "Invalid credentials or not an admin user."

    return render(request, 'admin_login.html', {'error': error})
