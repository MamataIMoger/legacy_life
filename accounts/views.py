from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from eligibility.models import EligibilityCheck, Hospital

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "Account created successfully")
        return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('dashboard')  # redirecting to dashboard after login
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out")
    return redirect('login')


@login_required
def dashboard(request):
    eligibility_history = EligibilityCheck.objects.filter(user=request.user).order_by('-checked_at')
    hospitals = Hospital.objects.all()
    latest_check = eligibility_history.first()

    result = None
    ineligibility_reason = None
    advice = None

    # Flags for journey timeline
    has_registered = True  # Always true since user is logged in
    has_checked_eligibility = False
    has_chosen_hospital = False
    has_certificate = False  # You can extend this later with actual certificate logic

    if latest_check:
        has_checked_eligibility = True

        if latest_check.is_eligible:
            result = "Eligible"
            advice = "You are eligible to donate organs. You can proceed with hospital registration."

            if latest_check.selected_hospital:
                has_chosen_hospital = True
                has_certificate = True  # For now, assume certificate is issued once hospital is selected
        else:
            result = "Ineligible"
            reasons = []
            if latest_check.chronic_disease:
                reasons.append("Chronic disease")
            if latest_check.infection:
                reasons.append("Active infection")
            if latest_check.recent_surgery:
                reasons.append("Recent surgery")
            if latest_check.cancer_history:
                reasons.append("Cancer history")
            if latest_check.substance_abuse:
                reasons.append("Substance abuse")
            if latest_check.pregnant:
                reasons.append("Currently pregnant")
            ineligibility_reason = ", ".join(reasons) if reasons else "Not specified"
            advice = "You are currently ineligible. Please consult a healthcare professional for advice."

    return render(request, 'dashboard.html', {
        'eligibility_history': eligibility_history,
        'hospitals': hospitals,
        'result': result,
        'ineligibility_reason': ineligibility_reason,
        'advice': advice,
        'has_registered': has_registered,
        'has_checked_eligibility': has_checked_eligibility,
        'has_chosen_hospital': has_chosen_hospital,
        'has_certificate': has_certificate,
    })
