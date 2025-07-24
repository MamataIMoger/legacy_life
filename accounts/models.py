# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3)
    organs_to_donate = models.TextField(help_text="Comma-separated list (e.g., Kidney, Liver)")
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Donor Profile"
