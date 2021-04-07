from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from vacancies.models import Company, Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            "title",
            "specialty",
            "skills",
            "description",
            "salary_min",
            "salary_max",
        )
        labels = {
            "title": "Название вакансии",
            "specialty": " Специализация",
            "skills": "Навыки",
            "description": "Описание вакансии",
            "salary_min": "Зарплата от",
            "salary_max": "Зарплата до",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.label_class = "mb-2 text-dark"
        self.helper.add_input(Submit("submit", "Сохранить", css_class="btn btn-primary btn-block"))
        self.helper.layout = Layout(
            Row(Column("title")),
            Row(
                Column("specialty"),
                Column("skills"),
            ),
            Row(Column("description")),
            Row(
                Column("salary_min"),
                Column("salary_max"),
            ),
        )


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            "name",
            "location",
            "description",
            "employee_count",
            "logo",
        )
        labels = {
            "name": "Название компании",
            "location": "Локация",
            "description": "Информация о компании",
            "employee_count": "Количество человек в компании",
            "logo": "Логотип",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.label_class = "mb-2 text-dark"
        self.helper.add_input(Submit("submit", "Сохранить", css_class="btn btn-primary btn-block"))
        self.helper.layout = Layout(
            Row(Column("name")),
            Row(
                Column("location"),
                Column("employee_count"),
            ),
            Row(Column("logo")),
            Row(Column("description")),
        )
