
from django.urls import path

from . import views

urlpatterns = [
    ## Define paths for the main projects page and create project formulary
    path("", views.index, name="index"),
    path("create_project", views.create_project, name="create_project"),
    path("get_team_users/<int:teamId>", views.get_team_users, name="get_team_users"),

    ## Define paths for the login, logout and register route 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    ## Define paths for the task and assign task route 
    path("tasks/", views.tasks, name="tasks"),
    path("create_task", views.create_task, name="create_task"),
    path("project_tasks/<int:project_id>/", views.project_tasks, name='project_tasks'),
    path('mark_task_as_completed/<int:task_id>/', views.mark_task_as_completed, name='mark_task_as_completed'),


    ## Define paths for the teams page and create teams formulary
    path("teams", views.teams, name="teams"),
    path("create_team", views.create_team, name="create_team"),
    path("team_projects/<int:team_id>/", views.team_projects, name='team_projects')
]
