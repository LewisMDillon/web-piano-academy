from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormCreateView.as_view(), name='contact_form'),
    path('list/', views.ContactListView.as_view(), name='contact_list'),
    path(
        '<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'
        ),
    path('<pk>/update', views.ContactUpdateView.as_view(), name='contact-update'),
    path('success/', views.ContactSuccess, name='contact_success'),

]
