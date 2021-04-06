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


class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=10)

    class Meta:
        model = Company
        fields = (
            "name",
            "location",
            "description",
            "employee_count",
        )
