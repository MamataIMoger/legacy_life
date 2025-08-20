from django.contrib import admin
from .models import ImportantDate

@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "description")
