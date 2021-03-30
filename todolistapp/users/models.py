from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FantasyTeam (models.Model):
    # team name
    team_name = models.CharField(max_length=100)

    # associated user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # created-date
    created_date = models.DateField()

    # modified-date
    last_modified_date = models.DateField()

