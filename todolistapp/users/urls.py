# users/urls.py

from django.conf.urls import url, include
from .views import dashboard, register, team_create, teams_view

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^teams/create", team_create, name="team_creation"),
    url(r"^teams/view", teams_view, name="teams_view"),
]