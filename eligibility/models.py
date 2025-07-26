from django.db import models

class EligibilityCheck(models.Model):
    age = models.IntegerField()
    bmi = models.FloatField()
    chronic_disease = models.BooleanField()
    infection = models.BooleanField()
    
    recent_surgery = models.BooleanField(default=False)
    cancer_history = models.BooleanField(default=False)
    substance_abuse = models.BooleanField(default=False)
    pregnant = models.BooleanField(default=False)

    is_eligible = models.BooleanField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check at {self.checked_at} - Eligible: {self.is_eligible}"
    
    def __str__(self):
        return f"Check at {self.checked_at} - Eligible: {self.is_eligible}"

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name
