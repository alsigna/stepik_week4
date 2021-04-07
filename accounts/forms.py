from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(max_length=128, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Регистрация", css_class="btn btn-primary btn-lg btn-block"))
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field("username", placeholder="Логин", autofocus="autofocus"),
            Field("first_name", placeholder="Имя"),
            Field("last_name", placeholder="Фамилия"),
            Field("email", placeholder="e-mail"),
            Field("password1", placeholder="Пароль"),
            Field("password2", placeholder="Подтвердите пароль"),
        )


class CrispyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["invalid_login"] = "Некорректные логин/пароль"
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Войти", css_class="btn btn-primary btn-lg btn-block"))
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field("username", placeholder="Имя пользователя", autofocus="autofocus"),
            Field("password", placeholder="Пароль"),
        )
