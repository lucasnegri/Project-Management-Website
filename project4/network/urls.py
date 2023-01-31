
from django.urls import path

from . import views

urlpatterns = [
    ## Define paths for the main projects page and create project formulary
    path("", views.index, name="index"),
    path("create_project", views.create_project, name="create_project"),

    ## Define paths for the login, logout and register route 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    ## Define paths for the task and assign task route 
    path("tasks", views.tasks, name="tasks"),
    path("create_task", views.create_task, name="create_task"),
    
    ## Define paths for the teams page and create teams formulary
    path("teams", views.teams, name="teams"),
    path("create_team", views.create_team, name="create_team")
]
