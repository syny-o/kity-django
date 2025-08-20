from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('api/portrait-photos/', views.send_portrait_photos_to_api, name='portrait-photos'),
    path('api/family-photos/', views.send_family_photos_to_api, name='family-photos'),
    path('api/pregnant-photos/', views.send_pregnant_photos_to_api, name='pregnant-photos'),
    path('api/wedding-photos/', views.send_wedding_photos_to_api, name='wedding-photos'),
    path('api/commerce-photos/', views.send_commerce_photos_to_api, name='commerce-photos'),
    path('api/contact-form/', views.receive_contact_from_api, name='contact-form'),
]