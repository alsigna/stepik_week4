from django.urls import path

from .views import (
    MyCompanyCreate,
    MyCompanyEdit,
    MyCompanyLetsstart,
    MyCompanyVacancyCreate,
    MyCompanyVacancyEdit,
    MyCompanyVacancyList,
)

urlpatterns = [
    path("mycompany/", MyCompanyEdit.as_view(), name="my_company"),
    path("mycompany/letsstart/", MyCompanyLetsstart.as_view(), name="my_company_letsstart"),
    path("mycompany/create/", MyCompanyCreate.as_view(), name="my_company_create"),
    path("mycompany/vacancies/", MyCompanyVacancyList.as_view(), name="my_company_vacancies"),
    path("mycompany/vacancies/create/", MyCompanyVacancyCreate.as_view(), name="my_company_vacancy_create"),
    path("mycompany/vacancies/<int:pk>/", MyCompanyVacancyEdit.as_view(), name="my_company_vacancy_edit"),
]
