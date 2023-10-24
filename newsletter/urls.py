from django.contrib import admin
from django.urls import path
from . import views
from .views import MailingListCreateView

urlpatterns = [
    path('', MailingListCreateView.as_view(), name='mailing-list-subscribe'),
]
