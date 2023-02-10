from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    color = models.CharField(max_length=7)
    members = models.ManyToManyField(User, related_name='teams', default=None, null=True,)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_teams')

    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super().save(*args, **kwargs)

    def completed_projects_count(self):
        return self.project_set.filter(is_completed=True).count()


class Project(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects', default=None, null=True,)
    color = models.CharField(max_length=7, default=None, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.color = self.team.color.lower()
        super().save(*args, **kwargs)

    def completed_tasks_count(self):
        return self.task_set.filter(is_completed=True).count()

    def is_all_tasks_completed(self):
        completed_tasks = self.task_set.filter(is_completed=True).count()
        total_tasks = self.task_set.count()
        return completed_tasks == total_tasks

class Task(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default=None, null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.color = self.project.color.lower()
        super().save(*args, **kwargs)
        if self.is_completed:
            if self.project.is_all_tasks_completed():
                self.project.is_completed = True
                self.project.save()