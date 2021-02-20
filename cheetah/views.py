from django.shortcuts import render
from django.contrib.auth.views import TemplateView
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
