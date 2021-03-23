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

class Player (models.Model):
    # Associated Team
    team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)

    # first name
    first_name = models.CharField(max_length=100)

    # last name
    last_name = models.CharField(max_length=100)

    # player id
    player_id = models.IntegerField()

    # stats - ppg
    points_per_game = models.FloatField()

    # stats - rpg
    rebounds_per_game = models.FloatField()

    # stats - apg
    assists_per_game = models.FloatField()

    # created-date
    created_date = models.DateField()

    # modified-date
    last_modified_date = models.DateField()
