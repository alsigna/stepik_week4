from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from vacancies.models import Company, Specialty, Vacancy

from .forms import ApplicationForm


class MainView(TemplateView):
    template_name = "vacancies/public/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialties"] = Specialty.objects.all().annotate(vacancies_count=Count("vacancies"))
        context["companies"] = Company.objects.all().annotate(vacancies_count=Count("vacancies"))
        return context


class VacanciesView(ListView):
    model = Vacancy
    template_name = "vacancies/public/vacancy_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        specialty = self.kwargs.get("slug", None)
        if specialty:
            context["title"] = Specialty.objects.get(code=specialty).title
        else:
            context["title"] = "Все вакансии"
        return context

    def get_queryset(self):
        queryset = Vacancy.objects.select_related("company")

        specialty = self.kwargs.get("slug", None)
        if specialty:
            return queryset.filter(specialty__code=specialty)
        else:
            return queryset


class VacancyView(DetailView):
    model = Vacancy
    template_name = "vacancies/public/vacancy_detail.html"

    def get_queryset(self):
        return super().get_queryset().select_related("company", "specialty")

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ApplicationForm()
        context["form"] = form
        return context

    def post(self, request, pk, **kwargs):
        form = ApplicationForm(data=request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = get_object_or_404(User, pk=request.user.pk)
            application.vacancy = get_object_or_404(Vacancy, pk=pk)
            application.save()
            return redirect(reverse("public:application_sent", kwargs={"pk": pk}))
        else:
            self.object = self.get_object()
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)


class ApplicationSentView(TemplateView):
    template_name = "vacancies/public/application_sent.html"


class CompanyView(DetailView):
    model = Company
    template_name = "vacancies/public/company_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("vacancies")


class SearchResultsView(ListView):
    model = Vacancy
    template_name = "vacancies/public/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Vacancy.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        else:
            object_list = Vacancy.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        context["search_string"] = query
        return context
