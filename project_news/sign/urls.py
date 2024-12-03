from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import BaseRegisterView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign_login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign_logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign_signup.html'),
         name='signup'),
]