from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Renders files in the database to be filled by user when submitting contact
    """
    class Meta:
        model = Contact
        fields = [
            'email',
            'name',
            'subject',
            'order_number',
            'message']

    def __init__(self, *args, **kwargs):
        """Renders placeholders for user properly fill forms fields"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email Address',
            'name': 'Name',
            'subject': 'Subject',
            'order_number': 'Order Number',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
            