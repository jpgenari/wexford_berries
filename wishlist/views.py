from django.shortcuts import render, redirect, get_list_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile

# Create your views here.
@login_required
def view_wishlist(request):
    """
    View to render wishlist content page
    """
    user = UserProfile.objects.get(user=request.user)
    wishlist_items = Wishlist.objects.filter(user=user)
    
    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})
