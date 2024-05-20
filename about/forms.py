from django import forms
from .models import AboutPage


class AboutPageForm(forms.ModelForm):
    """Form that renders field content to be edited on front end"""
    class Meta:
        model = AboutPage
        fields = ['content']
