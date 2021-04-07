#####################################################################
#       Existed users (login / password)                            #
#        - admin / admin                                            #
#        - user1 / 123                                              #
#        - user2 / 123                                              #
#        - ...                                                      #
#        - user8 / 123                                              #
#####################################################################

from conf.settings import MEDIA_COMPANY_IMAGE_DIR
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=128)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company", null=True)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)

    def delete(self, *args, **kwargs):
        self.picture.storage.delete(self.picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    picture = models.URLField(default="https://place-hold.it/100x60")

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=256)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=512)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vacancies", kwargs={"pk": self.pk})

    def clean(self):
        super().clean()
        if int(self.salary_min) >= int(self.salary_max):
            raise ValidationError({"salary_min": ValidationError("Значение должно быть меньше максимального")})
        return


class Application(models.Model):
    written_username = models.CharField(max_length=256)
    written_phone = PhoneNumberField()
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    def __str__(self):
        return f"{self.user.username}:{self.vacancy.title}"


class Resume(models.Model):
    class Grade(models.TextChoices):
        TRAINEE = "TRAINEE", _("Стажер")
        JUNIOR = "JUNIOR", _("Джуниор")
        MIDDLE = "MIDDLE", _("Миддл")
        SENIOR = "SENIOR", _("Синьор")
        LEAD = "LEAD", _("Лид")

    class Status(models.TextChoices):
        CLOSE = "CLOSE", _("Не ищу работу")
        PASSIVE = "PASSIVE", _("Рассматриваю предложения")
        ACTIVE = "ACTIVE", _("Ищу работу")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume")
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.CLOSE)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=32, choices=Grade.choices, default=Grade.TRAINEE)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return f"Resume: {self.user.username}-{self.specialty.code}"
