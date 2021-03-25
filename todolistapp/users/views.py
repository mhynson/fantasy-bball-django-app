from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import FantasyTeam, Player
from pprint import pprint
from datetime import datetime
# from crud import crud

import json

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        context = {
            "form": CustomUserCreationForm
        }
        return render(
            request, "users/register.html",
            context
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def team_create(request):
    teams = FantasyTeam.objects.all()

    # Load all players
    players = None
    with open('./players.json') as f:
        players = json.load(f)


    if request.method == "POST":

        print("=== user ===")
        pprint(request.user)

        print("=== POST ===")
        pprint(request.POST)

        # First check to see if the user is logged in.
        if request.user and request.user.is_authenticated:
            print("keep going...")

            # Extract the incoming team name from the incoming POST request.
            incoming_team_name = request.POST["fantasy-team-name"]
            user_id = request.user.id
            matching_teams = FantasyTeam.objects.filter(user=request.user)
            team_already_exists = False

            print("=== incoming team name ===")
            print(incoming_team_name)

            print("=== matching teams ===")
            print(matching_teams)

            # Loop through the list of teams to see if one matches the name of the incoming team name.
            for team in matching_teams:
                # Check to see if the team exists, and set it to a variable.
                team_already_exists = incoming_team_name == team.team_name
                # If there
                if team_already_exists:
                    break

            print("== does team already exists? ")
            print(team_already_exists)

            if team_already_exists:
                print("This team name is already taken! Please pick a different one.")
                # exit out of the function
                # return render(request, "teams/create.html", {
                #     "message": "This team name is already taken! Please pick a different one.",
                #     "players": players,
                #     "teams": teams,
                # })


            # Now, create the team object (based on the FantasyTeam Model) with the given team name and other attributes
            new_team = FantasyTeam(
                team_name=incoming_team_name,
                user=request.user,
                created_date=datetime.now(),
                last_modified_date=datetime.now(),
            )
            new_team.save()

            player_ids = list()
            count = 1
            while (count < 6):
                player_id = request.POST["fantasy-player-" + str(count)]
                player_ids.append(player_id)


                matching_player =  [player for player in players if player["id"] == player_id]
                print(" --- matching_player " + player_id + " ---")
                print(matching_player)

                count += 1


            print("=== player ids ===")
            print(player_ids)
            # print(new_team)


        else:
            print("The user is not logged in, so we cannot add a Team or Players.")


        print("user")
        print(request.user)

        # 1. Check to see if a user has a team with the same name
        # 2. If not, then add the team to the user
        # 3. Add the players to the team



    return render(request, "teams/create.html", {
        "players": players,
        "teams": teams
    })
# def lists(request):

#     if request.user and request.user.is_logged:
#         context = {
#             lists: user.full_list
#         }
#     return render(request, "users/lists.html")
