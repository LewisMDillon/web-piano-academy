from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('error400/', views.errortest400, name='errortest400'),
    path('error403/', views.errortest403, name='errortest403'),
    path('error404/', views.errortest404, name='errortest404'),
    path('error500/', views.errortest500, name='errortest500'),
]
