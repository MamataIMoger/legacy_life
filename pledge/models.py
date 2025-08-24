from django.db import models

class Pledge(models.Model):
    ORGAN_CHOICES = [
        ('Heart', 'Heart'),
        ('Kidneys', 'Kidneys'),
        ('Liver', 'Liver'),
        ('Lungs', 'Lungs'),
        ('Eyes', 'Eyes'),
        ('Skin', 'Skin'),
        ('All', 'All Organs'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    organs = models.CharField(max_length=100, choices=ORGAN_CHOICES)
    message = models.TextField(blank=True, null=True)
    date_pledged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} pledged to donate {self.organs}"
