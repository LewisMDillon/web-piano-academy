from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/<product_id>', views.product_detail, name='product_detail'),
]
