from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = render_to_string('confirmation_emails/contact_confirmation_subject.txt', {'email': contact.email})
            body = render_to_string('confirmation_emails/contact_confirmation_body.txt', {
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
            
            print(email)
            
            return redirect('success_view')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'contact_success.html')
