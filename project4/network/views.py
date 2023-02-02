from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User, Team, Project, Task

from .models import User

#------------------------------------------------------------------------------------#


## Define path to load the main page (projects)
def index(request):
    return render(request, "network/index.html")

## Define path to load the create project formulary
def create_project(request):
    if request.method == "GET":
        current_user = request.user
        user_teams = current_user.teams.all()
        context = {
            'user_teams': user_teams
        }
        return render(request, "network/create_project.html", context)
    else:
        name = request.POST["project_name"]
        objective = request.POST["project_objective"]
        selected_team = Team.objects.get(id=request.POST["selected_team"])
        selected_users = selected_team.members.all()
        project = Project(name=name, objective=objective, team=selected_team)
        project.save()
        project.members.set(selected_users)
        project.save()

        return 

#------------------------------------------------------------------------------------#


## Define path to load the tasks page
def tasks(request):
    return render(request, "network/tasks.html")

## Define path to load the create task formulary
def create_task(request):
    return render(request, "network/create_task.html")


#------------------------------------------------------------------------------------#


## Define path to load the teams page
def teams(request):
    current_user = request.user
    teams = current_user.teams.all()
    context = {
        'teams': teams
    }
    return render(request, "network/teams.html", context)

## Define path to load the create team formulary
def create_team(request):
    if request.method == "GET":
        registered_users = User.objects.all()
        registered_list = [{"username": user.username} for user in registered_users]
        
        objects = {
            "registered_list": registered_list
        }
        return render(request, "network/create_team.html", objects)
    else:
        name = request.POST["team_name"]
        objective = request.POST["team_objective"]
        color = request.POST["team_color"]
        selected_users = User.objects.filter(username__in=request.POST.getlist("user[]"))

        team = Team(name=name, objective=objective, color=color)
        team.save()
        team.members.set(selected_users)
        team.save()

        registered_users = User.objects.all()
        
        current_user = request.user
        teams = current_user.teams.all()
        context = {
            'teams': teams
        }
        return render(request, "network/teams.html", context)



#------------------------------------------------------------------------------------#



## Define path to the login page
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

## Define path to the logout route 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

## Define path to the register route 
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/login.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/login.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/login.html")
