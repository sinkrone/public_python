from django.urls import path

from . import views

app_name = "about"
urlpatterns = [
    path("", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]
