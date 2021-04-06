from django.urls import path

from .views import MyResumeCreate, MyResumeEdit, MyResumeLetsstart

urlpatterns = [
    path("myresume/", MyResumeEdit.as_view(), name="my_resume"),
    path("myresume/letsstart/", MyResumeLetsstart.as_view(), name="my_resume_letsstart"),
    path("myresume/create/", MyResumeCreate.as_view(), name="my_resume_create"),
]
