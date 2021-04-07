from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView
from vacancies.models import Company, Vacancy

from .forms import CompanyForm, VacancyForm

#####################################################################
#                       MyCompany Lets Start                        #
#####################################################################


class MyCompanyLetsstart(LoginRequiredMixin, TemplateView):
    template_name = "vacancies/company/my_company_letsstart.html"

    def get(self, request, *args, **kwargs):
        if Company.objects.filter(owner__pk=request.user.pk).first():
            return redirect(reverse("company:my_company"))
        return super().get(request, *args, **kwargs)


#####################################################################
#                              MyCompany                            #
#####################################################################


class MyCompanyCreate(LoginRequiredMixin, View):
    def get(self, request):
        company = Company.objects.filter(owner__pk=request.user.pk).first()
        if company:
            return redirect(reverse("company:my_company"))
        form = CompanyForm()
        return render(request, "vacancies/company/my_company_edit.html", {"form": form})

    def post(self, request):
        company = Company.objects.filter(owner__pk=request.user.pk).first()
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = get_object_or_404(User, pk=request.user.pk)
            company.save()
            messages.add_message(request, messages.INFO, "Данные сохранены")
            return redirect(reverse("company:my_company"))
        else:
            return render(request, "vacancies/company/my_company_edit.html", {"form": form})


class MyCompanyEdit(MyCompanyCreate):
    def get(self, request):
        company = Company.objects.filter(owner__pk=request.user.pk).first()
        if not company:
            return redirect(reverse("company:my_company_letsstart"))
        else:
            form = CompanyForm(instance=company)
            return render(request, "vacancies/company/my_company_edit.html", {"form": form})


#####################################################################
#                        MyCompany Vacancies                        #
#####################################################################


class MyCompanyVacancyList(LoginRequiredMixin, ListView):
    template_name = "vacancies/company/my_company_vacancies.html"

    def get_queryset(self):
        return Vacancy.objects.filter(
            company__owner__id=self.request.user.pk,
        ).annotate(application_count=Count("applications"))


class MyCompanyVacancyCreate(LoginRequiredMixin, View):
    def get(self, request, vacancy=None):
        form = VacancyForm(instance=vacancy)
        return render(
            request,
            "vacancies/company/my_company_vacancy_edit.html",
            {
                "form": form,
                "vacancy": vacancy,
            },
        )

    def post(self, request, **kwargs):
        vacancy_pk = self.kwargs.get("pk", None)
        vacancy = Vacancy.objects.filter(
            pk=vacancy_pk,
            company__owner__id=request.user.pk,
        ).first()
        form = VacancyForm(data=request.POST, instance=vacancy)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.filter(owner__id=request.user.pk).first()
            vacancy.save()
            messages.add_message(request, messages.INFO, "Данные сохранены")
            return redirect(reverse("company:my_company_vacancy_edit", kwargs={"pk": vacancy.pk}))

        else:
            return render(request, "vacancies/company/my_company_vacancy_edit.html", {"form": form})


class MyCompanyVacancyEdit(MyCompanyVacancyCreate):
    def get(self, request, pk):
        vacancy = (
            Vacancy.objects.filter(pk=pk, company__owner__id=request.user.pk)
            .prefetch_related("applications")
            .annotate(application_count=Count("applications"))
            .first()
        )
        if not vacancy:
            raise Http404
        return super().get(request, vacancy)
