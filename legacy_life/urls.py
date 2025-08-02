from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [

    path('admin/', admin.site.urls),

    # Home page
    path('', core_views.home, name='home'),

    # Admin login
    path('admin-login/', core_views.admin_login, name='admin_login'),

    # Accounts app (login, register, etc.)
    path('accounts/', include('accounts.urls')),

    # Eligibility check
    path('eligibility/', include('eligibility.urls')),

    # Myth Vs Facts page
    path('myths/', include('mythbuster.urls')),

    # Simulator
    path('simulator/', include('simulator.urls')),


]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
