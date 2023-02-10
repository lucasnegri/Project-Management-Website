from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import User, Team, Project, Task

from .models import User

#------------------------------------------------------------------------------------#

## Define path to load the teams page
def teams(request):
    current_user = request.user
    teams = current_user.teams.all()
    context = {
        'teams': teams,
    }
    return render(request, "network/teams.html", context)


## Define path to load the projects page of a specific team
def team_projects(request, team_id):
    team =Team.objects.get(id=team_id)
    projects = Project.objects.filter(team=team)
    message = "'{}' projects".format(team.name)
    return render(request, 'network/index.html',  {'projects': projects, 'message':message})


## Define path to process the "create_team" request
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
        
        current_user = request.user
        teams = current_user.teams.all()
        context = {
            'teams': teams
        }
        return render(request, "network/teams.html", context)


## Define path to process the "manage_team" request
def manage_team(request, teamId):
    team = get_object_or_404(Team, id=teamId)
    all_users = User.objects.all()
    return render(request, 'network/manage_team.html', {'team': team, 'all_users':all_users})
    

## Define path to remove the user from a specific team
def remove_member(request, member_id, team_id):
    # Add the member to the team
    member = User.objects.get(id=member_id)
    team = Team.objects.get(id=team_id)
    team.members.remove(member)

    # Render the updated member list
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return JsonResponse(context)


## Define path to add user to a specific team
def add_member(request, member_id, team_id):
    # Add the member to the team
    member = User.objects.get(id=member_id)
    team = Team.objects.get(id=team_id)
    team.members.add(member)

    # Render the updated member list
    all_users = User.objects.all().values()
    context = {"all_users":all_users}
    return JsonResponse(context)



#-=---------------------------------------------------------------------------#



## Define path to load the main page (projects)
def index(request):
    projects = request.user.projects.all()
    message= "All projects"
    context = {
        'projects': projects,
        'message':message
    }
    return render(request, "network/index.html", context)

## Pass user list when user select  team on create project form
def get_team_users(request, teamId):
    team = Team.objects.get(id=teamId)
    users = team.members.all()
    data = {
        "users": [{"username": user.username, "id": user.id} for user in users]
    }
    return JsonResponse(data)

## Define path to process the "create_project" request
def create_project(request):
    if request.method == "GET":
        context = {
            "registered_list": [{"username": user.username} for user in User.objects.all()],
            "user_teams": request.user.teams.all(),
        }
        return render(request, "network/create_project.html", context)
    else:
        name = request.POST.get("project_name")
        objective = request.POST.get("project_objective")
        selected_team = Team.objects.get(id=request.POST.get("selected_team"))
        selected_users = User.objects.filter(username__in=request.POST.getlist("user[]"))

        project = Project.objects.create(
            name=name, 
            objective=objective, 
            team=selected_team
        )
        project.members.set(selected_users)

        context = {
            "project_name":name,
            "project_objective":objective,
            "selected_users": selected_users,
            "selected_team": selected_team,
        }

        return redirect(index)




#------------------------------------------------------------------------------------#



## Define path to load the tasks page
def tasks(request):
    user_tasks = Task.objects.filter(assigned_to=request.user, is_completed=False)
    message = "All tasks"
    return render(request, "network/tasks.html", {'user_tasks': user_tasks, 'message':message})


## Define path to load the tasks from a specific project

def project_tasks(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    message = "{} project tasks".format(project.name)
    return render(request, 'network/tasks.html',  {'user_tasks': tasks, 'message':message})


## Define path to process the "create_taks" request
def create_task(request):
    if request.method == "GET": 
        project_id = request.GET.get('project_id')
        project = Project.objects.get(id=project_id)
        user_list = project.members.all()
        return render(request, "network/create_task.html", {'user_list': user_list, 'project_id':project_id})
    else:
        name = request.POST.get("task_name")
        objective = request.POST.get("task_objective")
        selected_user = User.objects.get(id=request.POST.get("selected_user"))

        project = Project.objects.get(id=request.POST.get("project_id"))

        task = Task.objects.create(name=name,objective=objective,project=project)
        task.assigned_to.add(selected_user)
        project.save()
        task.project.is_completed = False

        ##context = {"name":name, "objective":objective, "selected_user":selected_user, "project":project }
        return redirect(tasks)


## Mark task as completed
def mark_task_as_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()

    project = task.project
    if project.is_all_tasks_completed():
        project.is_completed = True
        project.save()

    return redirect(tasks)
#------------------------------------------------------------------------------------#




## Define path to load the teams page
def teams(request):
    current_user = request.user
    teams = current_user.teams.all()
    context = {
        'teams': teams,
    }
    return render(request, "network/teams.html", context)


## Define path to load the projects page of a specific team
def team_projects(request, team_id):
    team =Team.objects.get(id=team_id)
    projects = Project.objects.filter(team=team)
    message = "'{}' projects".format(team.name)
    return render(request, 'network/index.html',  {'projects': projects, 'message':message})


## Define path to process the "create_team" request
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

        team = Team(name=name, objective=objective, color=color, created_by=request.user)
        team.save()
        team.members.set(selected_users)
        
        current_user = request.user
        teams = current_user.teams.all()
        context = {
            'teams': teams
        }
        return render(request, "network/teams.html", context)


## Define path to process the "manage_team" request
def manage_team(request, teamId):
    team = get_object_or_404(Team, id=teamId)
    all_users = User.objects.all()

    return render(request, 'network/manage_team.html', {'team': team, 'all_users':all_users})
    

## Define path to remove the user from a specific team
def remove_member(request, team_id, user_id):
    team = get_object_or_404(Team, pk=team_id)
    user = get_object_or_404(User, pk=user_id)
    team.members.remove(user)
    all_users = User.objects.all()
    return render(request, 'network/manage_team.html', {'team': team, 'all_users':all_users})

## Define path to add user to a specific team

def add_member(request, team_id, user_id):
    team = get_object_or_404(Team, pk=team_id)
    user = get_object_or_404(User, pk=user_id)
    team.members.add(user)

    all_users = User.objects.all()
    return render(request, 'network/manage_team.html', {'team': team, 'all_users':all_users})




#-=---------------------------------------------------------------------------#



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
