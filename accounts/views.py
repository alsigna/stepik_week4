from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CrispyAuthenticationForm, SignUpForm


class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = CrispyAuthenticationForm
