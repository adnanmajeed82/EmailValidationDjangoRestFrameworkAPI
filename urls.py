# email_validation/urls.py

from django.urls import path
from .views import ValidatedEmailListCreateView, ValidatedEmailDetailView

urlpatterns = [
    path('validated-emails/', ValidatedEmailListCreateView.as_view(), name='validated-email-list-create'),
    path('validated-emails/<int:pk>/', ValidatedEmailDetailView.as_view(), name='validated-email-detail'),
]
