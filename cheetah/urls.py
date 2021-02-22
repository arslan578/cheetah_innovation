from django.urls import path
from cheetah.views import (
    SignUpView,
    IndexView,
    ServicesView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='SignUp'),
    path('', IndexView.as_view(), name='Index'),
    path('services', ServicesView.as_view(), name='Services')
]