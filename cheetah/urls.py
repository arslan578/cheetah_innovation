from django.urls import path
from cheetah.views import (
    SignUpView,
    IndexView,
    ServicesView,
    LoginView,
    UpdateProfileView,
    DeactivateUserView,
    DeeleteUserView
)

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='SignUp'),
    path('login', LoginView.as_view(), name='Login'),
    path('update-profile', UpdateProfileView.as_view(), name='Update-Profile'),
    path('deactivate', DeactivateUserView.as_view(), name='Deactivate'),
    path('delete', DeeleteUserView.as_view(), name='Delete'),
    path('', IndexView.as_view(), name='Index'),
    path('services', ServicesView.as_view(), name='Services')
]