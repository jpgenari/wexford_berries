from django.shortcuts import render, redirect, get_object_or_404, reverse
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


def add_and_delete_to_wishlist(request, item_id):
    """Add items to wishlist"""
    product = get_object_or_404(Product, pk=item_id)
    
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        wishlist_item = Wishlist.objects.filter(user=user, product=product).first()

        if wishlist_item:
            wishlist_item.delete()
            messages.warning(request, f'{product.name} removed from wishlist.')
        else:
            wishlist_item = Wishlist.objects.create(user=user, product=product)
            messages.success(request, f'{wishlist_item.product.name} successfully added to wishlist!')
    else:
        messages.warning(request, 'You must be logged in to add item to wishlist.')
        
    return redirect(reverse('product_detail', args=[item_id]))
        

@login_required
def delete_from_wishlist(request, item_id):
    """
    Remove items from wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(user=user, product=product)

    wishlist_item.delete()
    messages.success(request, f'{product.name} successfully removed from wishlist.')
    return redirect(reverse("view_wishlist"))
