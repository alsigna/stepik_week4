from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from vacancies.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            "written_username",
            "written_phone",
            "written_cover_letter",
        )
        labels = {
            "written_username": "Имя",
            "written_phone": "Телефон",
            "written_cover_letter": "Сопроводительное письмо",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.label_class = "mb-1"
        self.helper.add_input(Submit("submit", "Отправить заявку", css_class="btn btn-primary btn-block"))
        self.helper.layout = Layout(
            Row(
                Column("written_username"),
                Column("written_phone"),
            ),
            Row(Column("written_cover_letter")),
        )
