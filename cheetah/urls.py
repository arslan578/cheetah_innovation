from django.urls import path
from cheetah.views import (
    SignUpView,
    IndexView,
    ServicesView, LogoutView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', SignUpView.as_view(), name='SignUp'),
    path('index', login_required(IndexView.as_view()), name='Index'),
    path('services', login_required(ServicesView.as_view()), name='Services'),
    path('logout', login_required(LogoutView.as_view()), name="Logout")
]