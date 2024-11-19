# printer/urls.py

from django.urls import path
from .views import PrintView

urlpatterns = [
    path('', PrintView.as_view(), name='print_route'),
]
