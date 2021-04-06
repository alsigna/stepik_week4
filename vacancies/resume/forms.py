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
