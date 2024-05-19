from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    # path('add/<item_id>/', views.product_detail, name='product_detail'),
]
