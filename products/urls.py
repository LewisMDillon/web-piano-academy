from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path(
        'courses/<int:product_id>/',
        views.product_detail,
        name='product_detail'
        ),
    path('courses/add/', views.add_product, name='add_product'),
]
