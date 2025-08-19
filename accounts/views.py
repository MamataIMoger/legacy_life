from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from eligibility.models import EligibilityCheck, Hospital

# Additional imports for certificate
import qrcode
import base64
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


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
            return redirect('dashboard')
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

    # Journey timeline flags
    has_registered = True
    has_checked_eligibility = False
    has_chosen_hospital = False
    has_certificate = False

    if latest_check:
        has_checked_eligibility = True

        if latest_check.is_eligible:
            result = "Eligible"
            advice = "You are eligible to donate organs. You can proceed with hospital registration."

            if latest_check.selected_hospital:
                has_chosen_hospital = True
                has_certificate = True
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


@login_required
def generate_certificate(request):
    user = request.user

    latest_check = EligibilityCheck.objects.filter(
        user=user,
        is_eligible=True,
        selected_hospital__isnull=False
    ).first()

    if not latest_check:
        messages.error(request, "You must complete eligibility check and select hospital before downloading certificate.")
        return redirect('dashboard')

    # Create QR code for user verification URL (customize path if needed)
    profile_url = request.build_absolute_uri(f"/donor-profile/{user.id}/")
    qr = qrcode.make(profile_url)
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_base64 = base64.b64encode(qr_io.getvalue()).decode('utf-8')

    # Render HTML to PDF
    html = render_to_string("certificate_template.html", {
        "donor": user,
        "check": latest_check,
        "qr_code": qr_base64,
    })

    pdf_io = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_io)
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    response = HttpResponse(pdf_io.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="donor_certificate.pdf"'
    return response
