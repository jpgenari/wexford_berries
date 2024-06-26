from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact_view(request):
    """
    Renders the contact form on the front end.
    Also handles received form, saving it to the database, sending email
    confirmation email to user and redirecting success view.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = render_to_string(
                'contact/confirmation_emails/contact_confirmation_subject.txt',
                {'email': contact.email}
                )
            body = render_to_string(
                'contact/confirmation_emails/contact_confirmation_body.txt',
                {
                    'email': contact.email,
                    'name': contact.name,
                    'subject': contact.subject,
                    'order_number': contact.order_number,
                    'message': contact.message,
                    'order': {'date': contact.created_on}
                })
            email = EmailMessage(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [contact.email, settings.DEFAULT_FROM_EMAIL],
            )
            email.send(fail_silently=False)
            request.session['email'] = contact.email

            return redirect('success_view')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    """Renders message received confirmation to front end"""
    email = request.session.get('email', '')
    return render(request, 'contact/contact_success.html', {'email': email})
