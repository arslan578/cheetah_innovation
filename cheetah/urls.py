from django.urls import path
from cheetah.views import (
    SignUpView,
    IndexView,
    ServicesView
)

urlpatterns = [
    path('', SignUpView.as_view(), name='SignUp'),
    path('index', IndexView.as_view(), name='Index'),
    path('services', ServicesView.as_view(), name='Services'),
]