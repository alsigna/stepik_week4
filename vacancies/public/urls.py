from django.urls import path, re_path

from .views import ApplicationSentView, CompanyView, MainView, SearchResultsView, VacanciesView, VacancyView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("vacancies/cat/<int:pk>/sent", ApplicationSentView.as_view(), name="application_sent"),
    # через re_path для пробы было сделано, решил не убирать
    re_path(r"^vacancies/(?:cat/(?P<slug>\w+))?$", VacanciesView.as_view(), name="vacancies"),
    path("vacancies/<int:pk>", VacancyView.as_view(), name="vacancy"),
    path("companies/<int:pk>", CompanyView.as_view(), name="company"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
