from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View
from django.views.generic.base import TemplateView
from vacancies.models import Resume

from .forms import ResumeForm

#####################################################################
#                        MyResume Lets Start                        #
#####################################################################


class MyResumeLetsstart(LoginRequiredMixin, TemplateView):
    template_name = "vacancies/resume/my_resume_letsstart.html"

    def get(self, request, *args, **kwargs):
        if Resume.objects.filter(user__pk=request.user.pk).first():
            return redirect(reverse("resume:my_resume"))
        return super().get(request, *args, **kwargs)


#####################################################################
#                              MyResume                             #
#####################################################################


class MyResumeCreate(LoginRequiredMixin, View):
    def get(self, request):
        resume = Resume.objects.filter(user__pk=request.user.pk).first()
        if resume:
            return redirect(reverse("resume:my_resume"))
        form = ResumeForm()
        return render(request, "vacancies/resume/my_resume_edit.html", {"form": form})

    def post(self, request):
        resume = Resume.objects.filter(user__pk=request.user.pk).first()
        form = ResumeForm(data=request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = get_object_or_404(User, pk=request.user.pk)
            resume.save()
            return redirect(reverse("resume:my_resume"))
        else:
            return render(request, "vacancies/resume/my_resume_edit.html", {"form": form})


class MyResumeEdit(MyResumeCreate):
    def get(self, request):
        resume = Resume.objects.filter(user__pk=request.user.pk).first()
        if not resume:
            return redirect(reverse("resume:my_resume_letsstart"))
        else:
            form = ResumeForm(instance=resume)
            return render(request, "vacancies/resume/my_resume_edit.html", {"form": form})
