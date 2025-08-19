from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name


class EligibilityCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bmi = models.FloatField()
    chronic_disease = models.BooleanField(default=False)
    infection = models.BooleanField(default=False)
    recent_surgery = models.BooleanField(default=False)
    cancer_history = models.BooleanField(default=False)
    substance_abuse = models.BooleanField(default=False)
    pregnant = models.BooleanField(default=False)
    is_eligible = models.BooleanField(default=False)
    checked_at = models.DateTimeField(auto_now_add=True)

    selected_hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)

    transplant_type = models.CharField(max_length=100, blank=True, null=True)
    organ_donation_thoughts = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.checked_at.strftime('%Y-%m-%d')}"
