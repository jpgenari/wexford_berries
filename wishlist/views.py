from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def view_wishlist(request):
    """View to render wishlist content page to logged in user"""
    user = UserProfile.objects.get(user=request.user)
    wishlist_items = Wishlist.objects.filter(user=user)

    return render(
        request,
        "wishlist/wishlist.html",
        {"wishlist_items": wishlist_items}
    )


def add_and_delete_to_wishlist(request, item_id):
    """
    Checks if user is authenticated, checks items in user's wishlist,
    if item in wishlist gives option to delete, if not in wishlist gives
    option to add item to wish list.
    If user not authenticated asks to login in order to add item.
    After all actions issues a message to let user know.
    This views work with product_detail.html template from Products app.
    """
    product = get_object_or_404(Product, pk=item_id)

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        wishlist_item = Wishlist.objects.filter(
            user=user,
            product=product).first()

        if wishlist_item:
            wishlist_item.delete()
            messages.warning(request, f'{product.name} removed from wishlist.')
        else:
            wishlist_item = Wishlist.objects.create(user=user, product=product)
            messages.success(
                request,
                f'{wishlist_item.product.name} successfully added to wishlist!'
                )
    else:
        messages.warning(
            request, 'You must be logged in to add item to wishlist.'
            )

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def delete_from_wishlist(request, item_id):
    """
    Removes item from wishlist if user is logged in.
    """
    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(user=user, product=product)

    wishlist_item.delete()
    messages.success(
        request, f'{product.name} successfully removed from wishlist.'
        )
    return redirect(reverse("view_wishlist"))
