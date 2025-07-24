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
    path('myths/', include('mythbuster.urls')),

]
