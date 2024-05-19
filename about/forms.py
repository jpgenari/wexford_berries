from django import forms
from .models import AboutPage


class AboutPageForm(forms.ModelForm):

    class Meta:
        model = AboutPage
        fields = ['content']
