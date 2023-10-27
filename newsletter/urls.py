from django.contrib import admin
from django.urls import path
from . import views
from .views import MailingListCreateView, MailingListDeleteView

urlpatterns = [
    path('', MailingListCreateView.as_view(), name='mailing-list-subscribe'),
    path('unsub/', views.unsub, name='unsub'),
    path(
        '<int:pk>/delete/',
        MailingListDeleteView.as_view(), name='mailing-list-delete'
        ),
]
