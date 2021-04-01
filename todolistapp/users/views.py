from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import FantasyTeam
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


def teams_view(request):
    # Get all of the user's teams, so they can be displayed on the page.
    # This is the R of CRUD - to read from the database.

    # Fetch all teams.
    teams = FantasyTeam.objects.all()

    # Fetch only the current user's teams.
    # LEFT side (user) is the property name that belongs to the FantasyTeam class
    # RIGHT side (request.user) is the value that we want to match to.
    our_teams = FantasyTeam.objects.filter(user=request.user)

    # Matching team
    incoming_team_name = ""
    if request.GET and request.GET["team"]:
        incoming_team_name = request.GET["team"]
    matches = FantasyTeam.objects.filter(team_name=incoming_team_name)

    print("=== user ===")
    print(request.user.username)
    print(request.user.id)
    print("=== /user ===")

    context = {
        "teams": teams,
        "our_teams": our_teams,
        "user": request.user,
        "matches": matches,
    }

    return render(request, "teams/view-all.html", context)




def team_create(request):
    # DO something here to handle the request.
    print("===REQ METHOD ===")
    print(request.method)

    print("===USER FROM REQ ===")
    print(request.user.id)

    print("===GET DATA FROM REQ ===")
    print(request.GET)

    print("===POST DATA FROM REQ ===")
    print(request.POST)

    '''
        What do we have from the request parameter?
            - method (GET, POST)
            - user
            - GET data
            - POST data
    '''

    context = {
        "message": "Hello!"
    }

    if request.method == "POST":
        context["message"] = "Hi! This is a POST Request!"

        # Here we need to create an item in the DB using the POST data.

        # Step 1: Get the user-provided team name.
        incoming_team_name = request.POST["fantasy-team-name"]

        # Step 2: Create a new FantasyTeam instance and use the incoming_team_name for the team's name.
        team = FantasyTeam(
            team_name=incoming_team_name,
            user=request.user,
            created_date=datetime.now(),
            last_modified_date=datetime.now(),
        )

        # Step 3: Save the newly created team to the database.
        team.save()

        # Step 4: Create a message to display to the user.
        context["message"] = "Congratulations! You have successfully created your team (" + team.team_name + ")!"



    if request.method == "GET":
        context["message"] = "Hi! This is a GET Request!"


    return render(request, "teams/create.html", context)







# def team_create(request):
#     # Get all team objects using the Django ORM.
#     teams = FantasyTeam.objects.all()
#     print("-------- All TEAMS -------->")
#     for t in teams:
#         print(t.team_name)
#         print(t.created_date)
#         print(t.last_modified_date)
#     print("<!-------- All TEAMS --------")
#
#     # Load all players
#     players = None
#     with open('./players.json') as f:
#         players = json.load(f)
#
#
#     if request.method == "POST":
#
#         print("=== user ===")
#         pprint(request.user)
#
#         print("=== POST ===")
#         pprint(request.POST)
#
#         # First check to see if the user is logged in.
#         if request.user and request.user.is_authenticated:
#             print("keep going...")
#
#             # Extract the incoming team name from the incoming POST request.
#             incoming_team_name = request.POST["fantasy-team-name"]
#             user_id = request.user.id
#             matching_teams = FantasyTeam.objects.filter(user=request.user)
#             team_already_exists = False
#
#             print("=== incoming team name ===")
#             print(incoming_team_name)
#
#             print("=== matching teams ===")
#             print(matching_teams)
#
#             # Loop through the list of teams to see if one matches the name of the incoming team name.
#             for team in matching_teams:
#                 # Check to see if the team exists, and set it to a variable.
#                 team_already_exists = incoming_team_name == team.team_name
#                 # If there
#                 if team_already_exists:
#                     break
#
#             print("== does team already exists? ")
#             print(team_already_exists)
#
#             if team_already_exists:
#                 print("This team name is already taken! Please pick a different one.")
#                 # exit out of the function
#                 # return render(request, "teams/create.html", {
#                 #     "message": "This team name is already taken! Please pick a different one.",
#                 #     "players": players,
#                 #     "teams": teams,
#                 # })
#
#
#             # Now, create the team object (based on the FantasyTeam Model) with the given team name and other attributes
#             new_team = FantasyTeam(
#                 team_name=incoming_team_name,
#                 user=request.user,
#                 created_date=datetime.now(),
#                 last_modified_date=datetime.now(),
#             )
#             new_team.save()
#
#             player_ids = list()
#             count = 1
#             while (count < 6):
#                 player_id = request.POST["fantasy-player-" + str(count)]
#                 player_ids.append(player_id)
#
#
#                 matching_player =  [player for player in players if player["id"] == player_id]
#                 print(" --- matching_player " + player_id + " ---")
#                 print(matching_player)
#
#                 count += 1
#
#
#             print("=== player ids ===")
#             print(player_ids)
#             # print(new_team)
#
#
#         else:
#             print("The user is not logged in, so we cannot add a Team or Players.")
#
#
#         print("user")
#         print(request.user)
#
#         # 1. Check to see if a user has a team with the same name
#         # 2. If not, then add the team to the user
#         # 3. Add the players to the team
#
#
#
#     return render(request, "teams/create.html", {
#         "players": players,
#         "teams": teams
#     })
# def lists(request):

#     if request.user and request.user.is_logged:
#         context = {
#             lists: user.full_list
#         }
#     return render(request, "users/lists.html")
