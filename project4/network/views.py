from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User

#------------------------------------------------------------------------------------#


## Define path to load the main page (projects)
def index(request):
    return render(request, "network/index.html")

## Define path to load the create project formulary
def create_project(request):
    return render(request, "network/create_project.html")


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
    return render(request, "network/teams.html")

## Define path to load the create team formulary
def create_team(request):
    return render(request, "network/create_team.html")



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
