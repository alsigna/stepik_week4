from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include(("vacancies.public.urls", "public"), namespace="public")),
    path("", include(("vacancies.company.urls", "company"), namespace="company")),
    path("", include(("vacancies.resume.urls", "resume"), namespace="resume")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
