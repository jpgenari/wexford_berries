from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('edit/', views.edit_about, name='edit_about'),
]
