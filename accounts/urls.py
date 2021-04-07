from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import MyLoginView, SignupView

urlpatterns = [
    path("accounts/login/", MyLoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/signup/", SignupView.as_view(), name="signup"),
]
