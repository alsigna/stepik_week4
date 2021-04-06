from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
