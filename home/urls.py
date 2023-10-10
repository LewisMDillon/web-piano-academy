from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faqs/', views.faqs, name='faqs'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
]
