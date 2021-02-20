from django.shortcuts import render
from django.contrib.auth.views import TemplateView
# Create your views here.


class SignUpView(TemplateView):
    template_name = 'signup.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


