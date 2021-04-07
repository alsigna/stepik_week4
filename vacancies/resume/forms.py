from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from vacancies.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            "name",
            "surname",
            "status",
            "salary",
            "specialty",
            "grade",
            "education",
            "experience",
            "portfolio",
        )
        labels = {
            "name": "Имя",
            "surname": "Фамилия",
            "status": "Готовность к работе",
            "salary": "Желаемый оклад",
            "specialty": "Специализация",
            "grade": "Уровень",
            "education": "Образование",
            "experience": "Опыт работы",
            "portfolio": "Портфолио",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.label_class = "mb-2 text-dark"
        self.helper.add_input(Submit("submit", "Сохранить", css_class="btn btn-primary btn-block"))
        self.helper.layout = Layout(
            Row(
                Column("name"),
                Column("surname"),
            ),
            Row(
                Column("salary"),
                Column("status"),
            ),
            Row(
                Column("specialty"),
                Column("grade"),
            ),
            Row(Column("education")),
            Row(Column("experience")),
            Row(Column("portfolio")),
        )
