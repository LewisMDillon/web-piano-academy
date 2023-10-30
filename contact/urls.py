from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormCreateView.as_view(), name='contact_form'),
    path('success/', views.ContactSuccess, name='contact_success'),

]
