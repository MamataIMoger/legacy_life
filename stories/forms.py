# stories/forms.py
from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ["title", "author_name", "body", "cover"] 
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "author_name": forms.TextInput(attrs={"placeholder": "Your name (optional)"}),
            "body": forms.Textarea(attrs={"rows": 6, "placeholder": "Share your story..."}),
        }
