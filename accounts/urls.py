from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignupView

urlpatterns = [
    path("accounts/login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/signup/", SignupView.as_view(), name="signup"),
]
