from django.db import models

class Pledge(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ])
    organs_to_donate = models.TextField(help_text="List of organs/tissues you wish to pledge")
    message = models.TextField(blank=True, help_text="Optional message")
    date_pledged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
