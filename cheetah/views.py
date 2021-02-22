from django.shortcuts import render, redirect
from django.contrib.auth.views import TemplateView
# Create your views here.

from users.models import Users
import uuid
from django.contrib.auth import authenticate, login
from django.contrib import messages


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        try:
            user = Users(first_name=request.POST.get('first_name'),
                         last_name=request.POST.get('last_name'), email=request.POST.get('email'),
                         profession=request.POST.get('profession'), username=request.POST.get('email').split('@')[0] + str(uuid.uuid4()).split('-')[0],
                         phone_number=request.POST.get('phone_number')
                         )
            user.set_password(request.POST.get('password'))
            user.save()
            username = user.username
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Index')
        except Exception as e:
            messages.error(request, 'Email already exists')

        return redirect('SignUp')


class IndexView(TemplateView):
    template_name = 'index.html'


class ServicesView(TemplateView):
    template_name = 'services.html'
