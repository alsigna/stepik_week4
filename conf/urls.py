from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from vacancies.public.views import custom_500

handler500 = custom_500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("", include(("vacancies.public.urls", "public"), namespace="public")),
    path("", include(("vacancies.company.urls", "company"), namespace="company")),
    path("", include(("vacancies.resume.urls", "resume"), namespace="resume")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
