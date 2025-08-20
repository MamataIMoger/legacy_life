from django.contrib import admin
from .models import Pledge

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'blood_group', 'date_pledged')
