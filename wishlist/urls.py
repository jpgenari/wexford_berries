from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path(
        'add/<int:item_id>/',
        views.add_and_delete_to_wishlist,
        name='add_and_delete_to_wishlist'
        ),
    path(
        'delete/<int:item_id>/',
        views.delete_from_wishlist,
        name='delete_from_wishlist'
        ),
]
