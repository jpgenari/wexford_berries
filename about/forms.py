from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from .models import AboutPage


class AboutPageForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteInplaceWidget())

    class Meta:
        model = AboutPage
        fields = ['title', 'content']
