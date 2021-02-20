from django.urls import path
from cheetah.views import (
    DashboardView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard')
]