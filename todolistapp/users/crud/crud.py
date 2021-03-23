from todolistapp.users.models import FantasyTeam, Player
from pprint import pprint
from datetime import datetime

def create_team(team_name, user_id):
    # Now, create the team object (based on the FantasyTeam Model) with the given team name and other attributes
    new_team = FantasyTeam(
        team_name=team_name,
        user=user_id,
        created_date=datetime.now(),
        last_modified_date=datetime.now(),
    )
    new_team.save()