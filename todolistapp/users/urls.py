# users/urls.py

from django.conf.urls import url, include
from .views import dashboard, register, team_create

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^teams/create", team_create, name="team_create"),
]