from django.contrib import admin
from django.urls import path
from . import views
from .views import MailingListCreateView

urlpatterns = [
    path('', MailingListCreateView.as_view(), name='mailing-list-subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path(
        'unsubscribe/<str:email>',
        views.mailing_list_delete,
        name='mailing-list-unsubscribe'
        ),
]
