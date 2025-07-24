from django.contrib import admin
from .models import EligibilityCheck, Hospital

@admin.register(EligibilityCheck)
class EligibilityCheckAdmin(admin.ModelAdmin):
    list_display = ('age', 'bmi', 'chronic_disease', 'infection', 'is_eligible', 'checked_at')
    list_filter = ('is_eligible', 'chronic_disease', 'infection')
    ordering = ('-checked_at',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')
    search_fields = ('name',)
