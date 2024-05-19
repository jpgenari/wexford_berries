from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import AboutPage
from .forms import AboutPageForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    about_page = get_object_or_404(AboutPage, pk=1)
    return render(request, 'about/about.html', {'about_page': about_page})

@login_required
def edit_about(request):
    about_page = get_object_or_404(AboutPage, pk=1)
    if request.method == "POST":
        form = AboutPageForm(request.POST, instance=about_page)
        if form.is_valid():
            form.save()
        return redirect(reverse('about'))
    else:
        form = AboutPageForm(instance=about_page)
    
    return render(request, 'about/edit_about.html', {'form': form})
