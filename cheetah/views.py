import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import TemplateView
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from users.models import Users
import uuid
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.contrib.auth import logout


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        try:
            user = Users(first_name=request.POST.get('first_name'),
                         last_name=request.POST.get('last_name'), email=request.POST.get('email'),
                         profession=request.POST.get('profession'),
                         username=request.POST.get('email').split('@')[0] + str(uuid.uuid4()).split('-')[0],
                         phone_number=request.POST.get('phone_number'),
                         user_type='user'
                         )
            user.set_password(request.POST.get('password'))
            user.save()
            username = user.email
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Index')
        except Exception as e:
            messages.error(request, 'Email already exists')

        return redirect('SignUp')


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if not user.is_active:
                messages.error(request, 'Your account is deactivate')
                return redirect('Login')
            if user is not None:
                login(request, user)
                return redirect('Index')
            else:
                messages.error(request, 'Unable to login with provide credentials!')
                return redirect('Login')
        except Exception as e:
            messages.error(request, 'Unable to login with provide credentials!')
            return redirect('Login')


class IndexView(TemplateView):
    template_name = 'index.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class AboutUsView(TemplateView):
    template_name = 'about-us.html'


class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

class UpdateProfileView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            user = model_to_dict(request.user)
            # del user['password']
            return render(request, 'update-profile.html', context=user)
        except Exception as e:
            pass

    def post(self, request):
        context = dict()
        for key, value in request.POST.items():
            context[key] = value

        del context['csrfmiddlewaretoken']
        if Users.objects.filter(id=request.user.id).update(**context):
            return redirect('Index')
        else:
            messages.error(request, 'Profile Update Unsuccessful')


class DeactivateUserView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save()
        return redirect('Index')


class DeeleteUserView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return redirect('Index')
