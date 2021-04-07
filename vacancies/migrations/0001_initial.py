# Generated by Django 3.1.7 on 2021-04-07 17:45

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256)),
                ("location", models.CharField(max_length=128)),
                ("description", models.TextField()),
                ("employee_count", models.IntegerField()),
                ("logo", models.ImageField(upload_to="company_images")),
                (
                    "owner",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specialty",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=32)),
                ("title", models.CharField(max_length=128)),
                ("picture", models.URLField(default="https://place-hold.it/100x60")),
            ],
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=256)),
                ("skills", models.CharField(max_length=512)),
                ("description", models.TextField()),
                ("salary_min", models.IntegerField()),
                ("salary_max", models.IntegerField()),
                ("published_at", models.DateField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="vacancies.company",
                    ),
                ),
                (
                    "specialty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="vacancies.specialty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
                ("surname", models.CharField(max_length=128)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CLOSE", "Не ищу работу"),
                            ("PASSIVE", "Рассматриваю предложения"),
                            ("ACTIVE", "Ищу работу"),
                        ],
                        default="CLOSE",
                        max_length=32,
                    ),
                ),
                ("salary", models.IntegerField()),
                (
                    "grade",
                    models.CharField(
                        choices=[
                            ("TRAINEE", "Стажер"),
                            ("JUNIOR", "Джуниор"),
                            ("MIDDLE", "Миддл"),
                            ("SENIOR", "Синьор"),
                            ("LEAD", "Лид"),
                        ],
                        default="TRAINEE",
                        max_length=32,
                    ),
                ),
                ("education", models.TextField()),
                ("experience", models.TextField()),
                ("portfolio", models.URLField(blank=True)),
                (
                    "specialty",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vacancies.specialty",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("written_username", models.CharField(max_length=256)),
                ("written_phone", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ("written_cover_letter", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="vacancies.vacancy",
                    ),
                ),
            ],
        ),
    ]
